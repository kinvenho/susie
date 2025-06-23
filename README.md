# susie

A simple Python CLI tool to list and manage your last 20 shell commands.

## Features
- List your last 20 shell commands in a pretty table
- Run any command from your history by index
- Copy commands to your clipboard for easy reuse

## Installation

### From PyPI (recommended for most users)
After publishing, you (or anyone) can install globally with:

```sh
pip install susie
```

Or, for a user-only install (no admin rights):
```sh
pip install --user susie
```

### From Source (for development)
Clone the repo and install in editable mode:
```sh
git clone https://github.com/yourusername/susie.git
cd susie
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
pip install -e .
```

## Usage

### List your last 20 commands
```sh
susie list
```

### Run a command from history (by index)
```sh
susie run 1
```
- This will copy the command to your clipboard and execute it in your shell.

### How does it work?
- `susie` stores your last 20 commands in a file at `~/.susie_history`.
- You can manually add commands to this file, or extend the tool to automatically track your shell history.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Open a pull request

## License
[MIT](LICENSE)
