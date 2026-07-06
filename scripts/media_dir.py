import shutil
import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/raw/shows.csv")
MEDIA_DIR = Path("static/media")

df = pd.read_csv(CSV_PATH)
# Sort chronologically to map old folder numbers to new UUIDs
df_sorted = df.sort_values(['Date', 'Venue']).reset_index(drop=True)

for idx, row in df_sorted.iterrows():
    old_num = str(idx + 1)  # Current folder name
    new_uuid = row['Record_ID']
    
    old_path = MEDIA_DIR / old_num
    new_path = MEDIA_DIR / new_uuid
    
    if old_path.exists() and not new_path.exists():
        print(f"{old_num} → {new_uuid}")
        shutil.move(str(old_path), str(new_path))
    elif new_path.exists():
        print(f"{new_uuid} already exists, skipping.")
    else:
        print(f" Missing: {new_uuid} added.")
        new_path.mkdir(parents=True)

print("Done")