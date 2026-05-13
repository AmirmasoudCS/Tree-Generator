from pathlib import Path
from .config import DEFAULT_EXCLUDE_DIRS 
from .config import DEFAULT_EXCLUDE_FILES 
from .config import DEFAULT_EXCLUDE_SUFFIXES 
from .models import TreeNode


class TreePrinter:
    def __init__(
        self,
        root_path : str | Path = ".",
        exclude_dirs : list[str] | None = None,
        exclude_files : list[str] | None = None,
        exclude_suffixes : list[str] | None = None,
        show_hidden : bool = False,
        dirs_only : bool = False,
        show_size : bool = False,
        show_modified : bool = False,
        sort_by : str = "name"
    ):
        self.root = Path(root_path)
        self.show_hidden = show_hidden
        self.dirs_only = dirs_only
        self.show_size = show_size
        self.show_modified = show_modified
        self.sort_by = sort_by 

        self.exclude_dirs = (DEFAULT_EXCLUDE_DIRS if exclude_dirs is None else exclude_dirs)
        self.exclude_files = (DEFAULT_EXCLUDE_FILES if exclude_files is None else exclude_files)
        self.exclude_suffixes = (DEFAULT_EXCLUDE_SUFFIXES if exclude_suffixes is None else exclude_suffixes)

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
                if (
                    (self.show_hidden or not item.name.startswith("."))
                    and not self.should_exclude(item)
                    and (not self.dirs_only or item.is_dir())
                )
            ],
            key=self.sort_key
        )

    def build_tree(self, path: Path | None = None) -> TreeNode:
        path = path or self.root
        size = None
        modified = None
        if self.show_size or self.show_modified:
            stat = path.stat()
            if self.show_size and path.is_file():
                size = stat.st_size
            if self.show_modified:
                modified = stat.st_mtime
        node = TreeNode(
            name=path.name,
            is_dir=path.is_dir(),
                size=size,
                modified=modified
        )

        if path.is_dir():
            for item in self.get_items(path):
                child_node = self.build_tree(item)
                node.children.append(child_node)

        return node
    def sort_key(self, path : Path):
        if self.sort_by == "size":
            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            return (not path.is_dir(), -size, path.name.lower())
        elif self.sort_by == "modified":
            try:
                mtime = path.stat().st_mtime
            except OSError:
                mtime = 0 
            return (not path.is_dir(), -mtime, path.name.lower())
        return (not path.is_dir(), path.name.lower())