"""
Safe Input Logger - Task 04 (CodeCraft Internship)

This script is an EDUCATIONAL demo, not a real keylogger.

What it does:
- Asks the user to type text into the terminal.
- Each line typed by the user is saved to a local file (keystrokes.log).
- The user can clearly see the program and stop logging anytime
  by typing the EXIT command.

What it DOES NOT do:
- It does NOT capture system-wide keystrokes.
- It does NOT run hidden or in the background.
- It does NOT log other users' activity.

This is designed to demonstrate the concept of logging input
safely and ethically.
"""

from datetime import datetime
from pathlib import Path


LOG_FILE = Path("keystrokes.log")


def log_line(line: str) -> None:
    """Append a single line with timestamp to the log file."""
    with LOG_FILE.open("a", encoding="utf-8") as f:
        timestamp = datetime.now().isoformat(timespec="seconds")
        f.write(f"[{timestamp}] {line}\n")


def main() -> None:
    """Main function that collects user input and logs it."""
    print("=== Safe Input Logger (Task 04) ===")
    print("This tool only logs what YOU type into this window.")
    print("Type 'EXIT' (in caps) on a new line to stop logging.\n")

    while True:
        user_input = input("Type here (or EXIT to stop): ")

        if user_input == "EXIT":
            print("\nLogging stopped. All input saved to:", LOG_FILE.resolve())
            break

        # Log the line the user typed
        log_line(user_input)


if __name__ == "__main__":
    main()

