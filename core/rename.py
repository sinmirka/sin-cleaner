from pathlib import Path
import re

def normalize_filename(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = name.strip("_")
    return name

def get_renamed_path(path: Path) -> Path:
    normalized_stem = normalize_filename(path.stem)
    return path.with_name(normalized_stem + path.suffix.lower())