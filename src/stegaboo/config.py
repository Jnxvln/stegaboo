import json
from pathlib import Path

DEFAULT_OUTPUT_DIR = Path("outputs")
SETTINGS_PATH = Path("settings.json")

def load_settings():
    if SETTINGS_PATH.exists():
        with SETTINGS_PATH.open("r") as f:
            settings = json.load(f)
    return {}

def save_settings(settings: dict):
    with SETTINGS_PATH.open("w") as f:
        json.dump(settings, f, indent=4)

def get_output_path():
    settings = load_settings()
    return Path(settings.get("output_path", DEFAULT_OUTPUT_DIR))

def set_output_path(path: Path):
    settings = load_settings()
    settings["output_path"] = str(path)
    save_settings(settings)
    
