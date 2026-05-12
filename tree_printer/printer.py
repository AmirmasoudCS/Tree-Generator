from pathlib import Path
from .config import DEFAULT_EXCLUDE_DIRS 
from .config import DEFAULT_EXCLUDE_FILES 
from .config import DEFAULT_EXCLUDE_SUFFIXES 
from .models import TreeNode


class TreePrinter:
    def __init__(
        self,
        root_path : str | Path = ".",
        exclude_dirs=None,
        exclude_files=None,
        exclude_suffixes=None,
        show_hidden=False
    ):
        self.root = Path(root_path)
        self.show_hidden = show_hidden

        self.exclude_dirs = exclude_dirs or DEFAULT_EXCLUDE_DIRS
        self.exclude_files = exclude_files or DEFAULT_EXCLUDE_FILES
        self.exclude_suffixes = exclude_suffixes or DEFAULT_EXCLUDE_SUFFIXES

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
                if (self.show_hidden or not item.name.startswith(".")) and not self.should_exclude(item)
            ],
            key=lambda x: (x.is_file(), x.name.lower())
        )

    def build_tree(self, path: Path | None = None) -> TreeNode:
        path = path or self.root

        node = TreeNode(
            name=path.name,
            is_dir=path.is_dir(),
        )

        if path.is_dir():
            for item in self.get_items(path):
                child_node = self.build_tree(item)
                node.children.append(child_node)

        return node
