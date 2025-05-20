from PIL import Image
from pathlib import Path
from .config import get_output_path
from rich import print

TERMINATOR = "~~~END~~~"

def _message_to_bits(message: str) -> str:
    """Convert a message to a binary string."""
    message += TERMINATOR
    return ''.join(f"{ord(c):08b}" for c in message)

def encode_message(image_path: Path, message: str, output_file: Path = None):
    image = Image.open(image_path)

    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # If the input is a JPEG, warn and prepare to save as PNG
    if image_path.suffix.lower() in [".jpg", ".jpeg"]:
        print("[yellow]Warning: JPEG is lossy and unsafe for steganography. Converting to PNG.[/yellow]")
        image_path = image_path.with_suffix(".png")
        if output_file and output_file.suffix.lower() in [".jpg", ".jpeg"]:
            output_file = output_file.with_suffix(".png")

    # Process pixels
    pixels = list(image.getdata())
    bits = _message_to_bits(message)
    bit_idx = 0

    new_pixels = []
    for pixel in pixels:
        if bit_idx >= len(bits):
            new_pixels.append(pixel)
            continue

        r, g, b = pixel
        new_r = (r & ~1) | int(bits[bit_idx])       if bit_idx     < len(bits) else r
        new_g = (g & ~1) | int(bits[bit_idx + 1])   if bit_idx + 1 < len(bits) else g
        new_b = (b & ~1) | int(bits[bit_idx + 2])   if bit_idx + 2 < len(bits) else b

        new_pixels.append((new_r, new_g, new_b))
        bit_idx += 3

    if bit_idx < len(bits):
        print("[red]Error: Message too long for this image.[/red]")
        return

    image.putdata(new_pixels)

    # Determine save location
    output_path = output_file or get_output_path() / f"encoded_{image_path.name}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG")
    print(f"[green]Message encoded and saved to:[/green] [yellow]{output_path}[/yellow]")