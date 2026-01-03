from pathlib import Path
from core.resize import resize_image

print(
    resize_image(
        Path("ultrahd.jpg"),
        max_width=20,
        max_height=None,
        dry_run=False
    )
)
