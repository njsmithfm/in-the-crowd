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

# Define what counts as a "True" value (case insensitive)
true_values = {'TRUE', 'YES', 'VERDADERO'}
# Create a set-based check (much faster and accurate)
df['Free_Show'] = df['Free_Show'].astype(str).str.upper().apply(lambda x: x.strip() in true_values)

df['Notes'] = df['Notes'].fillna('')

df = df.dropna(subset=['Date','Venue','Borough'])

# 1. SORT BY DATE first (Oldest to Newest)
# This ensures the numbering follows the timeline
# Sorts by Date (primary) and Venue (secondary) for tie-breaking
df = df.sort_values(['Date', 'Venue'], ascending=[True, True])

# 2. Reset index so the row count starts fresh after sorting/dropping
df = df.reset_index(drop=True)

# 3. Create ONLY 'Show_Number' based on the sorted order
# We remove the line "df['Show Number'] = ..." entirely
df['Show_Number'] = range(1, len(df) + 1)

# Note: The column 'Free show?' from the CSV is kept as raw data.
# If you want to REMOVE the raw 'Free show?' column from the JSON output,
# uncomment the next line:
# df = df.drop(columns=['Free show?']) 
# But usually, it's better to keep the original data unless you are sure you don't need it.
# Since you mentioned "repeated datapoints", I assume you want to remove the snake_case versions 
# if they are duplicates of existing columns, but here you seem to have BOTH.
# If you specifically want to drop the CSV's raw "Free show?" column because you have "Free_Show":
df = df.drop(columns=['Free show?'], errors='ignore') 

records = df.to_dict(orient='records')

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, default=str)

print(f"Processed {len(records)} shows to {OUTPUT_JSON}")