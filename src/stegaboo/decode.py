from PIL import Image
from pathlib import Path
from rich import print

TERMINATOR = "~~~END~~~"

def _bits_to_message(bits: str) -> str:
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars)
    end_index = message.find(TERMINATOR)
    if end_index != -1:
        return message[:end_index]
    return message  # fallback if no terminator found


def decode_message(image_path: Path) -> str:
    image = Image.open(image_path)

    # Warn if the image is JPEG
    if image_path.suffix.lower() in [".jpg", ".jpeg"]:
        print("[yellow]Warning: JPEG is lossy. [/yellow][bold red]If this image was not encoded as a PNG originally, the hidden data may be corrupted.[/bold red]")

    # Convert to RGB if necessary
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
