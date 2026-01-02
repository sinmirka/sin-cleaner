from pathlib import Path
from core.info import get_file_info

info = get_file_info(Path("testmeta.jpg"))

print("NAME:", info.name)
print("SIZE:", info.size_human())
print("METADATA SECTIONS:")

for section, data in info.metadata.items():
    if section == "thumbnail":
        print(f" - {section}: {len(data)} bytes")
    else:
        print(f" - {section}: {len(data)} tags")
