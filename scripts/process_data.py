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
    if 'Chicago Underground Duo' in artist_lower:
        return ['Rob Mazurek','Chad Taylor','Chicago Underground Duo']
    if 'Pharoah Sanders' in artist_lower:
        return ['James Brandon Lewis','Joshua Abrams','Chad Taylor','Jeff Parker']
    if 'Anoushka Shankar' in artist_lower:
        return ['Anoushka Shankar','Sarathy Korwar']
    if 'Carlos Niño & Idris Ackamoor' in artist_lower:
        return ['Carlos Niño','Idris Ackamoor']
    if 'Carlos Niño & Saul Williams' in artist_lower:
        return ['Carlos Niño','Saul Williams']
    if 'Carlos Niño & Photay' in artist_lower:
        return ['Carlos Niño','Photay']
    if 'DOMi and JD Beck' in artist_lower:
        return ['DOMi','JD Beck']
    if 'The Comet Is Coming' in artist_lower:
        return ['Shabaka Hutchings','Danalogue','Betamax']
    if 'Parliament-Funkadelic' in artist_lower:
        return ['George Clinton','Parliament-Funkadelic', 'Parliament', 'Funkadelic']
    if 'Wu-Tang Clan' in artist_lower:
        return ['RZA','GZA','Young Dirty Bastard','Method Man','Raekwon','Ghostface Killah','Inspectah Deck','U-God','Masta Killa','Cappadonna']
    if 'Shabaka Hutchings & Esperanza Spalding' in artist_lower:
        return ['Shabaka Hutchings','Esperanza Spalding']
    if 'Vijay Iyer & Nicole Mitchell' in artist_lower:
        return ['Vijay Iyer','Nicole Mitchell']
    if 'Messthetics & James Brandon Lewis' in artist_lower:
        return ['Messthetics','James Brandon Lewis']
    if 'Raw Poetic & Damu The Fudgemunk' in artist_lower:
        return ['Raw Poetic','Damu The Fudgemunk']
    if 'Arooj Aftab, Vijay Iyer, & Shazhad Ismaily' in artist_lower:
        return ['Arooj Aftab','Vijay Iyer','Shazhad Ismaily']
    if 'Vijay Iyer & Arooj Aftab' in artist_lower:
        return ['Vijay Iyer','Arooj Aftab']
    if 'Armand Hammer' in artist_lower:
        return ['Armand Hammer','Billy Woods','Elucid','DJ Haram']
    
    
    
    
    return artist

df['Primary Artist'] = df['Artist'].apply(get_primary_artist)

# Sort chronologically, assign Show_Number (display-only)
df.sort_values(['Date', 'Venue'], ascending=[True, True], inplace=True)
df = df.reset_index(drop=True)
df['Bill_ID'] = df['Date'].astype(str) + '|' + df['Venue']
df['Show_Number'] = range(1, len(df) + 1)  # Recreated each run

df["Free_Show"] = (
    df["Free_Show"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("true")
)

# Build JSON output
records = []
for _, row in df.iterrows():
    record = row.dropna(how='all').to_dict()
    
    # Media lookup using STABLE Record_ID (not Show_Number!)
    record_id = row['Record_ID']
    image_dir = MEDIA_DIR / record_id
    media = {}
    
    if image_dir.exists():
        image_files = sorted(image_dir.glob("*.jpg"))
        if image_files:
            media['images'] = [f"media/{record_id}/{img.name}" for img in image_files]
    
    record['media'] = media if media else None
    
    records.append(record)

OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, default=str)

print(f"Processed {len(records)} shows to {OUTPUT_JSON}")




