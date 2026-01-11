# currently scrapped part of the app.

"""
import typer
from pathlib import Path
import sys

from core.info import get_file_info

app = typer.Typer()


@app.command(name="info")
def info(path: Path):
    info = get_file_info(path=path)

    typer.echo(f"Name: {info.name}")
    typer.echo(f"Size: {info.size_human()}")
    typer.echo(f"Extension: {info.extension}")
    typer.echo(f"Created: {info.created_at}")
    typer.echo(f"Modified: {info.modified_at}")

    if info.metadata:
        typer.echo("Metadata found:")
        for section, data in info.metadata.items():
            if section == "thumbnail":
                typer.echo(f" - {section}: {len(data)} bytes")
            else:
                typer.echo(f" - {section}: {len(data)} tags")
    else:
        typer.echo("Metadata: None")

def main():
    app()

if __name__ == "__main__":
    main()
"""