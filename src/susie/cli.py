import argparse
import os
import sys
import subprocess
from pathlib import Path
from rich.console import Console
from rich.table import Table
import pyperclip

HISTORY_FILE = Path.home() / ".susie_history"
MAX_HISTORY = 20
console = Console()

def load_history():
    if not HISTORY_FILE.exists():
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[-MAX_HISTORY:]

def save_history(commands):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(commands[-MAX_HISTORY:]))

def add_to_history(command):
    history = load_history()
    if command in history:
        history.remove(command)
    history.append(command)
    save_history(history)

def list_commands():
    history = load_history()
    table = Table(title="Susie Command History (last 20)")
    table.add_column("Index", justify="right", style="cyan", no_wrap=True)
    table.add_column("Command", style="magenta")
    for idx, cmd in enumerate(history, start=1):
        table.add_row(str(idx), cmd)
    console.print(table)

def run_command(index):
    history = load_history()
    if not (1 <= index <= len(history)):
        console.print(f"[red]Invalid index: {index}[/red]")
        sys.exit(1)
    command = history[index - 1]
    pyperclip.copy(command)
    console.print(f"[green]Copied to clipboard:[/green] {command}")
    try:
        subprocess.run(command, shell=True, check=True)
        add_to_history(command)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Command failed:[/red] {e}")

def main():
    parser = argparse.ArgumentParser(prog="susie", description="List and manage your last 20 shell commands.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List the last 20 commands.")

    run_parser = subparsers.add_parser("run", help="Run a command from history by index and copy to clipboard.")
    run_parser.add_argument("index", type=int, help="Index of the command to run (see 'susie list').")

    args = parser.parse_args()

    if args.command == "list":
        list_commands()
    elif args.command == "run":
        run_command(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
