# 🌲 Tree Printer
A Python CLI tool for generating clean and customizable directory tree structures directly from the terminal.

Supports filtering, sorting, icons, metadata display, and export to text files.
## 🧰 Requirements
- Python 3.10+
## 👀 Preview
```text
📁 Project
├── 📁 tree_printer
│   ├── 🐍 __init__.py
│   └── 🐍 logic.py
├── ⚖️ LICENSE
├── 🐍 main.py
├── ⚙️ pyproject.toml
└── 📘 README.md
```
## ✨ Features
- Recursive directory tree generation
- Configurable file and directory exclusions
- Hidden file filtering
- Maximum depth limiting
- Command-line interface with argparse
- Sorting by name, size, or modified date
- Export output to files
- Optional icons and metadata display
## 🚀 Installation
1. **Clone the repository**
```bash
git clone https://github.com/AmirmasoudCS/Tree-Printer.git
```
2. **Install the project**
```bash
pip install .
```
## ⌨️ Usage
**The examples below use `tp`, but `tree-printer` works identically.**
1. **Print *current* directory:**
```bash
tp . 
```
2. **Print a *specific* directory:**
```bash
tp goal_directory_path
```
3. ***Limit* recursion depth:**
```bash
tp --max-depth 2
```
or:
```bash
tp . -md 2
```
4. **Show *hidden* files:**
```bash
tp --show-hidden
```
or:
```bash
tp -sh
```
5. ***Write output* tree to a file instead of printing to the console:**
```bash
tp --output tree.txt
```
or:
```bash
tp -o tree.txt
```
6. Write only **directories** in the output tree:
```bash
tp --dirs-only
```
or:
```bash
tp -do
```
7. Sort entries by name:
```bash
tp --sort name
```
or:
```bash
tp -st name
```
8. Sort entries by size:
```bash
tp --sort size
```
or:
```bash
tp -st size
```
9. Sort entries by modified date:
```bash
tp --sort modified
```
or:
```bash
tp -st modified
```
## ⚙️ CLI Options
| Full Command | Alias | Description |
|:---:|:---:|:---:|
| `--max-depth` | `-md` | Limit recursion depth |
| `--show-hidden` | `-sh` | Include hidden files |
| `--output` | `-o` | Save output to a file |
| `--dirs-only` | `-do` | Prints only directories |
| `--exclude-dirs` | `-ed` | Exclude directories by name |
| `--exclude-files` | `-ef` | Exclude files by name |
| `--exclude-suffixes` | `-es` | Exclude files by suffixes |
| `--size` | `-s` | Show the size of files |
| `--modified` | `-m` | Show the modified date of files |
| `--icons` | `-i` | Show icons of each file or directory |
| `--sort` | `-st` | Sort entries by name, size or modified date |
## 📁 Project Structure
```
📁
├── 📁 tree_printer
│   ├── 🐍 __init__.py
│   ├── 🐍 cli.py
│   ├── 🐍 config.py
│   ├── 🐍 formatter.py
│   ├── 🐍 icons.py
│   ├── 🐍 models.py
│   └── 🐍 printer.py
├── ⚖️ LICENSE
├── 🐍 main.py
├── ⚙️ pyproject.toml
└── 📘 README.md
```
## 📌 Example Output
```text
├── project
│   ├── __init__.py
│   ├── database.py
│   └── logic.py
├── main.py
├── secrets.txt
└── image.png
```
```bash
tp -i
```
```text
📁
├── 📁 tree_printer
│   ├── 🐍 __init__.py
│   ├── 🐍 cli.py
│   ├── 🐍 config.py
│   ├── 🐍 formatter.py
│   ├── 🐍 icons.py
│   ├── 🐍 models.py
│   └── 🐍 printer.py
├── ⚖️ LICENSE
├── 🐍 main.py
├── ⚙️ pyproject.toml
└── 📘 README.md
```
```bash
tp -s
```
```text
├── tree_printer
│   ├── __init__.py (177 B)
│   ├── cli.py (3043 B)
│   ├── config.py (242 B)
│   ├── formatter.py (2162 B)
│   ├── icons.py (464 B)
│   ├── models.py (233 B)
│   └── printer.py (3131 B)
├── LICENSE (1088 B)
├── main.py (71 B)
├── pyproject.toml (434 B)
└── README.md (3796 B)
```
```bash
tp --sort modified --modified --icons
```
```text
📁  (2026-05-12 22:04)
├── 📁 tree_printer (2026-05-13 11:05)
│   ├── 🐍 cli.py (2026-05-13 12:04)
│   ├── 🐍 printer.py (2026-05-13 12:02)
│   ├── 🐍 formatter.py (2026-05-13 11:16)
│   ├── 🐍 icons.py (2026-05-13 11:11)
│   ├── 🐍 models.py (2026-05-13 10:16)
│   ├── 🐍 config.py (2026-05-12 22:09)
│   └── 🐍 __init__.py (2026-05-12 19:11)
├── 📘 README.md (2026-05-13 12:29)
├── ⚙️ pyproject.toml (2026-05-12 22:03)
├── 🐍 main.py (2026-05-12 19:30)
└── ⚖️ LICENSE (2026-05-11 15:11)
```
## ⚖️ License
**Licensed under the MIT License. See [LICENSE](LICENSE) for details.**