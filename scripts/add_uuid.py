#!/usr/bin/env python3
# scripts/setup_new_records.py

import uuid
import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/raw/shows.csv")
MEDIA_DIR = Path("static/media")

# Load CSV
df = pd.read_csv(CSV_PATH)

if 'Record_ID' not in df.columns:
    print("❌ Record_ID column not found in CSV!")
    exit(1)

# Find rows missing Record_ID
missing_ids = df[df['Record_ID'].isna()]

if len(missing_ids) == 0:
    print("All records already have Record_IDs.")
    exit(0)

print(f"Found {len(missing_ids)} record(s) missing Record_ID:")

for idx, row in missing_ids.iterrows():
    # Generate UUID
    new_uuid = str(uuid.uuid4())[:8]
    
    # Create media folder
    folder_path = MEDIA_DIR / new_uuid
    folder_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n✓ Assigned {new_uuid} to: {row['Artist']} ({row['Date']})")
    print(f"  Media folder created: {folder_path}")

# Update dataframe with new UUIDs and save
for idx, row in missing_ids.iterrows():
    new_uuid = str(uuid.uuid4())[:8]
    df.at[idx, 'Record_ID'] = new_uuid
    (MEDIA_DIR / new_uuid).mkdir(parents=True, exist_ok=True)

df.to_csv(CSV_PATH, index=False)
print(f"\n Updated {CSV_PATH} with {len(missing_ids)} new Record_IDs")