import typer
from pathlib import Path
from rich import print
from .config import get_output_path, set_output_path

app = typer.Typer(help="Stegaboo CLI: Hide your secrets in plain sight.")

@app.command()
def encode(
    image_path: Path,
    message: str,
    output_file: Path = typer.Option(None, "--output-file", "-o", help="Custom output file path"),
):
    """Encode a message into an image."""
    print("🚧 [bold yellow]Encoding not yet implemented.[/bold yellow] 🚧")
    
@app.command()
def decode(
    image_path: Path
):
    """Decode a message from an image."""
    print("🚧 [bold yellow]Decoding not yet implemented.[/bold yellow] 🚧")
    
@app.command()
def where():
    """Show the current output path."""
    output_path = get_output_path()
    print(f"[green]Current output path:[/green] {output_path}")
    
@app.command()
def set(
    what: str = typer.Argument(..., help="What to set (e.g. 'where')"),
    value: Path = typer.Argument(..., help="The new value")
):
    """Set configuration values, such like output path."""
    if what.lower() == "where":
        set_output_path(value)
        print(f"[cyan]Default output path set to:[/cyan] {value}")
    else:
        print(f"[red]Unknown setting: \"[bold yellow]{what}[/bold yellow]\"[/red]")