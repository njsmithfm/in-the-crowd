import pandas as pd
import json
from pathlib import Path

RAW_CSV = Path("data/raw/shows.csv")
OUTPUT_JSON = Path("public/data/shows.json")

OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW_CSV)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Year'] = df['Date'].dt.year.astype('Int64')
df['Month'] = df['Date'].dt.month.astype('Int64')
df['Day'] = df['Date'].dt.day_name()


df['Artist'] = df['Artist'].str.strip()

def get_primary_artist(artist):
    if pd.isna(artist):
        return None
    artist_lower = artist.lower()
    if 'antarctigo' in artist_lower:
        return 'Jeff Rosenstock','Chris Farren'
    if 'irreversible entanglements' in artist_lower:
        return 'Moor Mother'
    if 'chicago underground' in artist_lower:
        return 'Rob Mazurek','Chad Taylor'
    if 'Pharoah Sanders' in artist_lower:
        return ''
    return artist

df['Primary Artist'] = df['Artist'].apply(get_primary_artist)

df['Free_Show'] = df['Free show?'].astype(str).str.upper().str.contains('TRUE').astype(bool)

df['Notes'] = df['Notes'].fillna('')

df = df.dropna(subset=['Date','Venue','Borough'])

# Reset index to ensure clean sequential numbers after dropping NaNs
df = df.reset_index(drop=True)
# Create the Show Number column (1-based index)
df['Show_Number'] = range(1, len(df) + 1)
# --- ADD THIS BLOCK ENDS HERE ---

df['Show Number'] = df['Show_Number'].astype(int)

records = df.to_dict(orient='records')
                    
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, default=str)

print(f"Processed {len(records)} shows to {OUTPUT_JSON}")
