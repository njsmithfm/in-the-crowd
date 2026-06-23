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
        return 'Jeff Rosenstock','Chris Farren','Antarctigo Vespucci'
    if 'irreversible entanglements' in artist_lower:
        return 'Moor Mother','Irreversible Entanglements'
    if 'chicago underground' in artist_lower:
        return 'Rob Mazurek','Chad Taylor','Chicago Underground Duo'
    if 'Pharoah Sanders' in artist_lower:
        return 'James Brandon Lewis','Joshua Abrams','Chad Taylor','Jeff Parker'
    return artist

df['Primary Artist'] = df['Artist'].apply(get_primary_artist)

# Define truth values for english and spanish
true_values = {'TRUE', 'YES', 'VERDADERO'}

df['Free_Show'] = df['Free_Show'].astype(str).str.upper().apply(lambda x: x.strip() in true_values)

df['Notes'] = df['Notes'].fillna('')

df = df.dropna(subset=['Date','Venue','Borough'])


df = df.sort_values(['Date', 'Venue'], ascending=[True, True])

df = df.reset_index(drop=True)


df['Show_Number'] = range(1, len(df) + 1)


df = df.drop(columns=['Free show?'], errors='ignore') 

records = df.to_dict(orient='records')

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, default=str)

print(f"Processed {len(records)} shows to {OUTPUT_JSON}")