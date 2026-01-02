from pathlib import Path
from core.info import get_file_info

path = Path("test.txt")

info = get_file_info(path)

print("RAW OBJECT:")
print(info)
print()

print("FIELDS:")
print("Name:", info.name)
print("Extension:", info.extension)
print("Size (bytes):", info.size_bytes)
print("Size (human):", info.size_human())
print("Created:", info.created_at)
print("Modified:", info.modified_at)
