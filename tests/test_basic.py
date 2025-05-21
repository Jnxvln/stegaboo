from pathlib import Path
from stegaboo.encode import encode_message
from stegaboo.decode import decode_message

# Paths
SOURCE_IMAGE = Path("lil_boo.png")
ENCODED_IMAGE = Path("outputs/test_encoded.png")
TEST_MESSAGE = "Stegaboo test successful!"

def test_encode_decode_roundtrip():
    """Test that a message can be encoded and decoded successfully."""
    encode_message(SOURCE_IMAGE, TEST_MESSAGE, ENCODED_IMAGE)
    decoded = decode_message(ENCODED_IMAGE)
    assert decoded == TEST_MESSAGE
