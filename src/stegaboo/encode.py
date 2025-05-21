from PIL import Image
from pathlib import Path
from .config import get_output_path
from rich import print
from rich.panel import Panel
from unicodedata import normalize

TERMINATOR = "~~~END~~~"

def _message_to_bits(message: str) -> str:
    """Convert a message to a binary string."""
    message += TERMINATOR
    return ''.join(f"{ord(c):08b}" for c in message)

def encode_message(image_path: Path, message: str, output_file: Path = None, force: bool = False):
    """Encode a message into an image using Least Significant Bit (LSB) steganography."""
    image = Image.open(image_path)
    
    # Normalize the message to ASCII
    safe_message = normalize("NFKD", message).encode("ascii", "ignore").decode("ascii")

    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # If the input is a JPEG, warn and prepare to save as PNG
    if image_path.suffix.lower() in [".jpg", ".jpeg"]:
        if not force:
            print("\n[yellow]Warning: JPEG is lossy and unsafe for steganography. Converting to PNG.[/yellow]")
            image_path = image_path.with_suffix(".png")
            if output_file and output_file.suffix.lower() in [".jpg", ".jpeg"]:
                output_file = output_file.with_suffix(".png")
        else:
            print("[red]⚠ You are forcing JPEG encoding. Hidden data may be corrupted on save![/red]")

    # Process pixels
    pixels = list(image.getdata())
    bits = _message_to_bits(safe_message)
    bit_idx = 0

    # Check if the image is large enough to hold the message
    new_pixels = []
    for pixel in pixels:
        if bit_idx >= len(bits):
            new_pixels.append(pixel)
            continue

        # Set the least significant bit of each color component to the corresponding bit from the message
        r, g, b = pixel
        new_r = (r & ~1) | int(bits[bit_idx])       if bit_idx     < len(bits) else r
        new_g = (g & ~1) | int(bits[bit_idx + 1])   if bit_idx + 1 < len(bits) else g
        new_b = (b & ~1) | int(bits[bit_idx + 2])   if bit_idx + 2 < len(bits) else b

        # Append the new pixel to the list
        new_pixels.append((new_r, new_g, new_b))
        bit_idx += 3

    # Check if all bits have been used
    if bit_idx < len(bits):
        print("\n[red]Error: Message too long for this image.[/red]")
        return

    # Save the modified image
    image.putdata(new_pixels)

    # Determine save location
    output_path = output_file or get_output_path() / f"encoded_{image_path.name}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG")
    
    # Success message and show output path
    print('\n')
    msg = Panel.fit(
        f"[bold green]✓ Message successfully encoded![/bold green]\nSaved to: {output_path}",
        title="[cyan]StegaBoo[/cyan]",
        border_style="green"
    )
    print(msg)
    print('\n')