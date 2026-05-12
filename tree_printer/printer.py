
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
        self.exclude_dirs = exclude_dirs or set()
        self.exclude_files = exclude_files or set()
        self.exclude_suffixes = exclude_suffixes or set()
    def should_exclude(self, path: Path) -> bool:
        return (
            path.name in self.exclude_dirs
            or path.name in self.exclude_files
            or path.suffix in self.exclude_suffixes
        )
    def get_items(self, path: Path) -> list[Path]:
        return sorted(
            [
                item
                for item in path.iterdir()
                if not self.should_exclude(item)
            ],
            key=lambda x: (x.is_file(), x.name.lower())
        )
    def generate_tree(
        self,
        path: Path | None = None,
        prefix: str = ""
    ) -> list[str]:
        path = path or self.root
        lines = []
        items = self.get_items(path)
        for index, item in enumerate(items):
            is_last = index == len(items) - 1
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + item.name)
            if item.is_dir():
                extension = "    " if is_last else "│   "
                lines.extend(
                    self.generate_tree(
                        item,
                        prefix + extension
                    )
                )
        return lines
