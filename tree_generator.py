from pathlib import Path


class TreePrinter:
    def __init__(
        self,
        root_path=".",
        exclude_dirs=None,
        exclude_files=None,
        exclude_suffixes=None,
    ):
        self.root = Path(root_path)

        self.exclude_dirs = exclude_dirs or {
            ".ipynb_checkpoints",
            "__pycache__",
            ".git",
            "build",
            "dist",
            ".venv",
            "venv"
        }

        self.exclude_files = exclude_files or {
            ".DS_Store",
            "Thumbs.db",
            "tree_generator.py",
            "tree_structure.txt",
            "imageEncryptor.spec",
        }

        self.exclude_suffixes = exclude_suffixes or {
            ".pyc",
        }

    def should_exclude(self, path: Path) -> bool:
        return (
            path.name in self.exclude_dirs
            or path.name in self.exclude_files
            or path.suffix in self.exclude_suffixes
        )

    def get_items(self, path: Path):
        items = []

        for item in sorted(
            path.iterdir(),
            key=lambda x: (x.is_file(), x.name.lower())
        ):
            if not self.should_exclude(item):
                items.append(item)

        return items

    def print_tree(self, path=None, prefix=""):
        path = path or self.root
        items = self.get_items(path)

        for index, item in enumerate(items):
            is_last = index == len(items) - 1

            connector = "└── " if is_last else "├── "
            print(prefix + connector + item.name)

            if item.is_dir():
                extension = "    " if is_last else "│   "
                self.print_tree(item, prefix + extension)

    def display(self):
        print(self.root.resolve())
        print(".")
        self.print_tree()


if __name__ == "__main__":
    tree_printer = TreePrinter()
    tree_printer.display()
