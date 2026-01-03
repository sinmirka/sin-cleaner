from pathlib import Path
from core.resize import resize_image

print(
    resize_image(
        Path("photo.png"),
        max_width=11,
        max_height=None,
        dry_run=False
    )
)
