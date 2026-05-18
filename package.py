#!/usr/bin/env python3
import zipfile
import os

SOURCE = "running-coach"
OUTPUT = "running-coach.zip"

with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(SOURCE):
        for file in files:
            path = os.path.join(root, file)
            zf.write(path)
            print(f"  adding: {path}")

print(f"\nCreated {OUTPUT}")
