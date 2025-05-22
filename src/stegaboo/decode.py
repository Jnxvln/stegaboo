from PIL import Image, UnidentifiedImageError
from pathlib import Path
import typer
from rich import print

TERMINATOR = "~~~END~~~"

def decode_message(image_path: Path) -> str:
    """Decodes a hidden message from an image using Least Significant Bit (LSB) steganography."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"\n[bold red]❌ File not found:[/bold red] [not bold yellow]{image_path}[/not bold yellow]\n")
        raise typer.Exit(code=1)
    except UnidentifiedImageError:
        print(f"\n[bold red]❌ Not a valid image file:[/bold red] [not bold yellow]{image_path}[/not bold yellow]\n")
        raise typer.Exit(code=1)

    if image_path.suffix.lower() in [".jpg", ".jpeg"]:
        print("[yellow]Warning: JPEG is lossy.[/yellow] [bold red]If this image was not encoded as a PNG originally, the hidden data may be corrupted.[/bold red]")

    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = list(image.getdata())
    bits = ""
    chars = []

    for pixel in pixels:
        for channel in pixel[:3]:
            bits += str(channel & 1)
            if len(bits) >= 8:
                byte = bits[:8]
                bits = bits[8:]
                char = chr(int(byte, 2))
                chars.append(char)

                if ''.join(chars[-len(TERMINATOR):]) == TERMINATOR:
                    return ''.join(chars[:-len(TERMINATOR)])

                if len(chars) > 10000:
                    return "[Warning] Message may be corrupted or missing a terminator."

    return "[Warning] No hidden message found."
