# 👻 Stegaboo

*A playful CLI tool for hiding harmless secrets in plain sight using image steganography.*

---

## ✨ Features

- Encode hidden messages into PNG images
- Decode messages from images (with warning for lossy formats like JPEG)
- Custom output paths with fallback to defaults
- Stylized Rich + Typer CLI output
- Sample images included for quick testing
- Helpful splash screen and command hints

---

## 🚀 Installation

Clone the repo and install in editable mode:

```bash
git clone https://github.com/Jnxvln/stegaboo.git
cd stegaboo
python -m venv .venv
source .venv/bin/activate        # or .venv\Scripts\activate on Windows
pip install -e .
```

---

## 🎯 Try It Out

```bash
stegaboo                     # Shows splash screen
stegaboo encode --help       # Shows encoding options
stegaboo decode --help       # Shows decoding options
```

We’ve included two sample images:

| Image               | Description                  |
|--------------------|------------------------------|
| `lil_boo.png`       | Use this to practice encoding |
| `outputs/note_boo.png` | Already encoded with a message |

---

### 🧪 Example Commands

```bash
stegaboo decode outputs/note_boo.png
stegaboo encode lil_boo.png "I see you, boo!"
```

```bash
stegaboo decode outputs/note_boo.png --save-message "./secret_boo.txt"
stegaboo encode lil_boo.png "I see you, boo!" -o "outputs/encoded_boo.png"
```

---

## ⚠️ Safety Notice

Stegaboo is a playful tool for **non-sensitive** secrets only.  
Do **not** use this to hide personal, private, or critical information. It's for fun, not for security.

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🛠️ Roadmap

Coming soon!
---

## ✨ Credits

Created by [UncompiledSelf](https://buymeacoffee.com/uncompiledself) with inspiration, ghosts, and a little Rich magic 👻  
Powered by [Typer](https://typer.tiangolo.com/), [Rich](https://rich.readthedocs.io/), and [Pillow](https://python-pillow.org/)

## 👻 A Token for the Ghost

If Stegaboo made you smile, whisper, or mutter “okay that’s kinda cool”...  
You can tip the ghost here:

[**☕ Buy Me a Coffee**](https://buymeacoffee.com/uncompiledself)

> _Even spirits run on caffeine and validation._
