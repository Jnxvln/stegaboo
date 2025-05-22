from pathlib import Path
import json
from rich import print

SETTINGS_PATH = Path("settings.json")
DEFAULT_OUTPUT_DIR = Path("outputs")

def load_settings():
    if SETTINGS_PATH.exists():
        try:
            with SETTINGS_PATH.open("r") as f:
                return json.load(f), False
        except json.JSONDecodeError:
            print("[yellow]⚠️ Warning: settings.json is invalid. Using defaults.[/yellow]")
            return {}, True
    return {}, True

def save_settings(settings: dict, first_time=False):
    if first_time or not SETTINGS_PATH.exists():
        print("[cyan]📁 Creating settings.json for the first time... 🥳[/cyan]")
    with SETTINGS_PATH.open("w") as f:
        json.dump(settings, f, indent=4)

def get_output_path():
    settings, _ = load_settings()
    return Path(settings.get("output_path", DEFAULT_OUTPUT_DIR))

def set_output_path(path: Path):
    settings, first_time = load_settings()
    settings["output_path"] = str(path)
    save_settings(settings, first_time=first_time)