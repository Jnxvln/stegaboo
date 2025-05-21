import sys
import typer
from typing import Optional
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.console import Console
from .config import get_output_path, set_output_path
from .encode import encode_message
from .decode import decode_message
from .ui import show_splash
from . import __version__

app = typer.Typer(help="👻 Stegaboo CLI: A playful way to hide harmless secrets in plain sight.")

app.version = __version__

console = Console()

def main():
    """Custom entrypoint to show splash if no command is passed."""
    from typer.main import get_command

    if "--version" in sys.argv or "-v" in sys.argv:
        print(__version__)
        sys.exit(0)

    if len(sys.argv) == 1:
        show_splash()
        sys.exit(0)

    cli = get_command(app)
    cli()

@app.command()
def encode(
    image_path: Path,
    message: str,
    output_file: Path = typer.Option(None, "--output-file", "-o", help="Custom output file path"),
    force: bool = typer.Option(False, "--force", "-f", help="Force encoding into lossy formats like JPEG")
):
    """Encode a message into an image."""
    encode_message(image_path, message, output_file, force)
    
@app.command()
def decode(
    image_path: Path,
    save_message: Optional[Path] = typer.Option(
        None, "--save-message", "-s", help="Optional path to save the decoded message."
    )
):
    """Decode a message from an image."""
    message = decode_message(image_path)

    if save_message:
        save_message.parent.mkdir(parents=True, exist_ok=True)
        save_message.write_text(message)
        print('\n')
        
        msg = Panel.fit(
            f"[bold green]🗝️  Message decoded and saved to:[/bold green]\n[yellow]{save_message}[/yellow]",
            title="[cyan]Stegaboo[/cyan]",
            border_style="green"
        )
        print(msg)
        print('\n')
    else:
        print('\n')
        msg = Panel.fit(
            f"[bold green]🗝️  Decoded message:[/bold green]\n{message}",
            title="[cyan]Stegaboo[/cyan]",
            border_style="green"
        )
        print(msg)
        print('\n')
    
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