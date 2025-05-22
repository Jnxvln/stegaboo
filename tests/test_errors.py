import pytest
from pathlib import Path
from typer.testing import CliRunner
from stegaboo.cli import app

runner = CliRunner()

def test_decode_missing_file():
    result = runner.invoke(app, ["decode", "tests/assets/nope.png"])
    assert result.exit_code != 0
    assert "not found" in result.stdout

def test_encode_missing_file():
    result = runner.invoke(app, ["encode", "tests/assets/derp_derp.png", "Hi there"])
    assert result.exit_code != 0
    assert "not found" in result.stdout

def test_decode_invalid_image():
    # Create a fake image file
    bad_file = Path("tests/assets/not_an_image.txt")
    bad_file.write_text("This is not an image.")

    result = runner.invoke(app, ["decode", str(bad_file)])
    assert result.exit_code != 0
    assert "Not a valid image" in result.stdout

    bad_file.unlink()  # Clean up
