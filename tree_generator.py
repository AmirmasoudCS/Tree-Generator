from pathlib import Path

exclude_dirs = {'.ipynb_checkpoints', '__pycache__', '.git', 'build', 'dist'}
exclude_files = {'.DS_Store', 'Thumbs.db', 'tree_generator.py', 'tree_structure.txt', 'imageEncryptor.spec'}
exclude_suffixes = {'.pyc'}

def print_tree(path, prefix=""):
    items = []
    for p in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if p.name in exclude_dirs:
            continue
        if p.name in exclude_files:
            continue
        if p.suffix in exclude_suffixes:
            continue
        items.append(p)

    for i, item in enumerate(items):
        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if i == len(items) - 1 else "│   "
            print_tree(item, prefix + extension)

root = Path(".")
print(root.resolve())
print(".")
print_tree(root)
