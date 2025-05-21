from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text
from rich import box

console = Console()

def show_splash():
    header = Text()
    header.append("👻 Stegaboo", style="bold cyan")
    header.append("\n")
    header.append("A playful way to hide harmless secrets in plain sight.\n", style="italic white")
    header.append("Built with Typer + Rich | by UncompiledSelf (May, 2025)", style="dim")
    
    # Text to use lil_boo.png and note_boo.png as examples
    help_text = Text()
    help_text.append("\nFeel free to use ")
    help_text.append("lil_boo.png", style="bold green")
    help_text.append(" to practice encoding,\nand ")
    help_text.append("outputs/note_boo.png", style="bold green")
    help_text.append(" to practice decoding.\n\n")

    # List of quick commands
    help_text.append("📖 Quick commands:\n")
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo --help", style="bold yellow")
    help_text.append(" → overview of all commands\n")

    # Text to get help on encoding
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo encode --help", style="bold yellow")
    help_text.append(" → help encoding a message\n")

    # Text to get help on decoding
    help_text.append("  • ", style="dim")
    help_text.append("stegaboo decode --help", style="bold yellow")
    help_text.append(" → help decoding an image\n\n")
    
    # Text for Examples to try
    help_text.append("🎯 Try these examples:\n")
    help_text.append("  stegaboo decode outputs/note_boo.png\n", style="green")
    help_text.append('  stegaboo encode lil_boo.png "I see you, boo!"\n\n', style="green")

    help_text.append("  stegaboo decode outputs/note_boo.png --save-message ./secret_boo.txt\n", style="yellow")
    help_text.append('  stegaboo encode lil_boo.png "I see you, boo!" -o outputs/encoded_boo.png\n\n', style="yellow")

    # Text to check README
    help_text.append("See the README for more details.", style="dim")

    body = Group(header, help_text)

    splash = Panel.fit(
        body,
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 4),
    )

    console.print(splash)