from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text
from rich import box

console = Console()

TITLE_STYLE = "bold yellow"
DESCRIPTION_STYLE = "italic white"
METADATA_STYLE = "dim"
SUBTITLE_STYLE = "bold magenta"
IMG_SAMPLE_STYLE = "bold blue"
CODE_STYLE = "green"
README_STYLE = "not bold white"
SUPPORT_TITLE_STYLE = "bold yellow"
SUPPORT_DESCRIPTION_STYLE = "not bold blue"
SUPPORT_LINK_STYLE = "bold yellow"

def show_splash():
    header = Text()
    header.append("👻 STEGABOO\n", style=TITLE_STYLE)
    header.append("\n")
    header.append("A playful way to hide harmless secrets in plain sight.\n", style=DESCRIPTION_STYLE)
    header.append("Built with Typer + Rich | by UncompiledSelf (May, 2025)", style=METADATA_STYLE)
    
    # Text to use lil_boo.png and note_boo.png as examples
    help_text = Text()
    help_text.append("\n│ Feel free to use ")
    help_text.append("lil_boo.png", style=IMG_SAMPLE_STYLE)
    help_text.append(" to practice encoding,\n│ and ")
    help_text.append("outputs/note_boo.png", style=IMG_SAMPLE_STYLE)
    help_text.append(" to practice decoding.\n\n")

    # List of quick commands
    help_text.append("📖 Quick commands:\n", style=SUBTITLE_STYLE)
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo --help", style=CODE_STYLE)
    help_text.append(" → overview of all commands\n")

    # Text to get help on encoding
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo encode --help", style=CODE_STYLE)
    help_text.append(" → help encoding a message\n")

    # Text to get help on decoding
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo decode --help", style=CODE_STYLE)
    help_text.append(" → help decoding an image\n\n")
    
    # Text for Examples to try
    help_text.append("🎯 Try these examples:\n", style=SUBTITLE_STYLE)
    help_text.append("  stegaboo decode outputs/note_boo.png\n", style=CODE_STYLE)
    help_text.append('  stegaboo encode lil_boo.png "I see you, boo!"\n\n', style=CODE_STYLE)
    
    help_text.append("  Or with custom outputs:\n", style=SUBTITLE_STYLE)
    
    help_text.append("  stegaboo decode outputs/note_boo.png --save-message ./secret_boo.txt\n", style=CODE_STYLE)
    help_text.append('  stegaboo encode lil_boo.png "I see you, boo!" -o outputs/encoded_boo.png\n\n', style=CODE_STYLE)
    
    # Text to check README
    help_text.append("See the README for more details.\n", style=README_STYLE)
    
    # Text for BMAC support
    bmac_text = Text("👻 A Token for the Ghost\n", style=SUPPORT_TITLE_STYLE)
    bmac_text.append("   If Stegaboo made you smile, whisper, or mutter “okay that’s kinda cool”, \n   You can tip the ghost here:\n", style=SUPPORT_DESCRIPTION_STYLE)
    bmac_text.append("\n   ☕ https://www.buymeacoffee.com/uncompiledself\n\n", style=SUPPORT_LINK_STYLE)


    body = Group(header, help_text, bmac_text)

    splash = Panel.fit(
        body,
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 4),
    )

    console.print(splash)