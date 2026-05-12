# 🌲 Tree Printer
A Python CLI tool for generating clean directory tree structures.
Built with an OOP architecture featuring recursive tree models, formatting abstraction, and CLI support.
## ✨ Features
- Recursive directory tree generation
- Configurable exclusions
- Hidden file filtering
- Maximum depth limiting
- Output to text files
- Clean CLI interface
## 🚀 Installation
1. **Clone the repository**
```bash
git clone https://github.com/AmirmasoudCS/Tree-Generator.git
```
2. Run the program
```bash
python main.py
```
## ⌨️ Usage
1. Print current directory:
```bash
python main.py 
```
2. Print a specific directory:
```bash
python main.py goal_directory_path
```
3. Limit recursion depth:
```bash
python main.py --max-depth 2
```
or easier:
```bash
python main.py . -md 2
```
4. Show hidden files:
```bash
python main.py --show-hidden
```
or easier:
```bash
python main.py -sh
```
5. Write output tree to a file instead of printing to the console:
```bash
python main.py --output tree.txt
```
or easier:
```bash
python main.py -o tree.txt
```
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
└── README.md
```
## ⚖️ License
This project is licensed under the MIT [LICENSE](LICENSE). This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software. The software is provided “as is”, without warranty of any kind, express or implied, and in no event shall the authors be liable for any claim, damages, or other liability arising from its use.