#!/usr/bin/env python3
# scripts/process_shows.py

import json
import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/raw/shows.csv")
OUTPUT_JSON = Path("public/data/shows.json")
MEDIA_DIR = Path("static/media")

df = pd.read_csv(CSV_PATH)

# Date parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year.astype('Int64')
df['Month'] = df['Date'].dt.month.astype('Int64')
df['Day'] = df['Date'].dt.day_name()

# Boolean normalization
true_values = {'TRUE', 'YES', 'VERDADERO'}
df['Free_Show'] = df['Free_Show'].astype(str).str.upper().apply(lambda x: x.strip() in true_values)
df['Notes'] = df['Notes'].fillna('')

# Artist cleanup
df['Artist'] = df['Artist'].str.strip()

def get_primary_artist(artist):
    if pd.isna(artist):
        return None
    artist_lower = artist.lower()
    if 'antarctigo' in artist_lower:
        return ['Jeff Rosenstock','Chris Farren','Antarctigo Vespucci']
    if 'irreversible entanglements' in artist_lower:
        return ['Moor Mother','Irreversible Entanglements']
    if 'chicago underground' in artist_lower:
        return ['Rob Mazurek','Chad Taylor','Chicago Underground Duo']
    if 'pharoah sanders' in artist_lower:
        return ['James Brandon Lewis','Joshua Abrams','Chad Taylor','Jeff Parker']
    return artist

df['Primary Artist'] = df['Artist'].apply(get_primary_artist)

# Sort chronologically, assign Show_Number (display-only)
df.sort_values(['Date', 'Venue'], ascending=[True, True], inplace=True)
df = df.reset_index(drop=True)
df['Bill_ID'] = df['Date'].astype(str) + '|' + df['Venue']
df['Show_Number'] = range(1, len(df) + 1)  # Recreated each run

# Build JSON output
records = []
for _, row in df.iterrows():
    record = row.dropna(how='all').to_dict()
    
    # Media lookup using STABLE Record_ID (not Show_Number!)
    record_id = row['Record_ID']
    media_dir = MEDIA_DIR / record_id
    media = {}
    
    if media_dir.exists():
        video_file = media_dir / f"{record_id}.mp4"
        if video_file.exists():
            media['video'] = f"/media/{record_id}/{record_id}.mp4"
        image_files = sorted(media_dir.glob("*.jpg"))
        if image_files:
            media['images'] = [f"/media/{record_id}/{img.name}" for img in image_files]
    
    record['media'] = media if media else None
    
    # Cleanup temp columns
    for col in ['Free show?', 'mediaPath']:
        record.pop(col, None)
    
    records.append(record)

OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, default=str)

print(f"Processed {len(records)} shows to {OUTPUT_JSON}")