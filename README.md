# Stegaboo 🦭

A playful image steganography CLI tool built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Jnxvln/stegaboo.git
cd stegaboo
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install the project in editable mode:

```bash
pip install -e .
```

## Usage

```bash
stegaboo encode path/to/image.png "your secret message"
stegaboo decode path/to/image.png
stegaboo where
stegaboo set where path/to/folder
```
