# 🌲 Tree Generator
A Python CLI tool for generating clean directory tree structures.
Built with an OOP architecture featuring recursive tree models, formatting abstraction, and CLI support.
## ✨ Features
- Recursive directory tree generation
- Configurable file and directories exclusions
- Hidden file filtering
- Maximum depth limiting
- Output to text files
- Command-line interface with argparse
## 🚀 Installation
1. **Clone the repository**
```bash
git clone https://github.com/AmirmasoudCS/Tree-Generator.git
```
2. **Install the project**
```bash
pip install .
```
## ⌨️ Usage
1. **Print *current* directory:**
```bash
tree-printer . 
```
  or:
```bash
tp .
```
2. **Print a *specific* directory:**
```bash
tree-printer goal_directory_path
```
  or:
```bash
tp goal_directory_path
```
3. ***Limit* recursion depth:**
```bash
tree-printer --max-depth 2
```
  or:
```bash
tp . -md 2
```
4. **Show *hidden* files:**
```bash
tree-printer --show-hidden
```
  or:
```bash
tp -sh
```
5. ***Write output* tree to a file instead of printing to the console:**
```bash
tree-printer --output tree.txt
```
  or:
```bash
tp -o tree.txt
```
## ⚙️ CLI Options
| Full Command | Alias | Description |
|---|---|---|
| `--max-depth` | `-md` | Limit recursion depth |
| `--show-hidden` | `-sh` | Include hidden files |
| `--output` | `-o` | Save output to a file |

## 📁 Project Structure
```
├── tree_printer
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── formatter.py
│   ├── models.py
│   └── printer.py
├── LICENSE
├── main.py
├── pyproject.toml
└── README.md
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
## ⚖️ License
This project is licensed under the MIT [LICENSE](LICENSE). This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software. The software is provided “as is”, without warranty of any kind, express or implied, and in no event shall the authors be liable for any claim, damages, or other liability arising from its use.