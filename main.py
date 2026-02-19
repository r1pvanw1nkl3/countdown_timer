import argparse
import time
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel

# Large ASCII art for digits 0-9 and ":"
DIGITS = {
    '0': [
        "  ██████  ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        "  ██████  "
    ],
    '1': [
        "   ████   ",
        "  █████   ",
        "    ███   ",
        "    ███   ",
        "    ███   ",
        "    ███   ",
        "    ███   ",
        "  ███████ "
    ],
    '2': [
        " ████████ ",
        "      ███ ",
        "      ███ ",
        "  ███████ ",
        " ███      ",
        " ███      ",
        " ███      ",
        " ████████ "
    ],
    '3': [
        " ████████ ",
        "      ███ ",
        "      ███ ",
        "  ███████ ",
        "      ███ ",
        "      ███ ",
        "      ███ ",
        " ████████ "
    ],
    '4': [
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        " ████████ ",
        "      ███ ",
        "      ███ ",
        "      ███ ",
        "      ███ "
    ],
    '5': [
        " ████████ ",
        " ███      ",
        " ███      ",
        " ████████ ",
        "      ███ ",
        "      ███ ",
        "      ███ ",
        " ████████ "
    ],
    '6': [
        "  ██████  ",
        " ███      ",
        " ███      ",
        " ███████  ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        "  ██████  "
    ],
    '7': [
        " ████████ ",
        "      ███ ",
        "     ███  ",
        "    ███   ",
        "   ███    ",
        "  ███     ",
        " ███      ",
        " ███      "
    ],
    '8': [
        "  ██████  ",
        " ███  ███ ",
        " ███  ███ ",
        "  ██████  ",
        " ███  ███ ",
        " ███  ███ ",
        " ███  ███ ",
        "  ██████  "
    ],
    '9': [
        "  ██████  ",
        " ███  ███ ",
        " ███  ███ ",
        "  ███████ ",
        "      ███ ",
        "      ███ ",
        "      ███ ",
        "  ██████  "
    ],
    ':': [
        "          ",
        "   ████   ",
        "   ████   ",
        "          ",
        "          ",
        "   ████   ",
        "   ████   ",
        "          "
    ]
}

def format_time(seconds):
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02}:{secs:02}"

def get_ascii_time(time_str):
    height = 8
    lines = [""] * height
    for char in time_str:
        digit_lines = DIGITS.get(char, ["          "] * height)
        for i in range(height):
            lines[i] += digit_lines[i] + " "
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Presentation Countdown Timer")
    parser.add_argument("timer", type=float, nargs='?', default=15.0, help="Total timer length in minutes (default: 15)")
    parser.add_argument("yellow", type=float, nargs='?', default=5.0, help="Yellow warning threshold in minutes (default: 5)")
    parser.add_argument("red", type=float, nargs='?', default=1.0, help="Red warning threshold in minutes (default: 1)")
    
    args = parser.parse_args()
    
    total_seconds = int(args.timer * 60)
    yellow_seconds = int(args.yellow * 60)
    red_seconds = int(args.red * 60)
    
    console = Console()
    
    try:
        remaining = total_seconds
        while remaining >= 0:
            time_str = format_time(remaining)
            ascii_art = get_ascii_time(time_str)
            
            # Determine color
            if remaining <= red_seconds:
                color = "red"
            elif remaining <= yellow_seconds:
                color = "yellow"
            else:
                color = "white"
            
            # Clear and render
            console.clear()
            
            text = Text(ascii_art, style=color)
            centered_text = Align.center(text, vertical="middle")
            
            console.print(centered_text)
            
            if remaining == 0:
                break
                
            time.sleep(1)
            remaining -= 1
            
        console.print("\n")
        prompt = Text("Time's up! Press Enter to exit...", style="bold blink red")
        console.print(Align.center(prompt))
        input()
        
    except KeyboardInterrupt:
        console.print("\nTimer stopped.", style="bold red")

if __name__ == "__main__":
    main()
