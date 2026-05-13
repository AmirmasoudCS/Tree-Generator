from datetime import datetime
from tree_printer.models import TreeNode
from pathlib import Path
from .icons import FILE_ICONS, DEFAULT_FILE_ICON

class TreeFormatter:
    def __init__(
            self,
            show_icons : bool = False,
    ):
        self.show_icons = show_icons
    def format_metadata(self, node : TreeNode) -> str:
        metadata = []
        if node.size is not None:
            metadata.append(f"{node.size} B")
        if node.modified is not None:
            formatted_date = datetime.fromtimestamp(node.modified).strftime("%Y-%m-%d %H:%M")
            metadata.append(formatted_date)
        label = f"{self.get_icon(node)}{node.name}"
        if metadata:
            return f"{label} ({' | '.join(metadata)})"
        return label
    def format(
            self,
            node : TreeNode,
            prefix : str = "",
            depth : int = 0,
            max_depth : int | None = None
    ) -> list[str]:
        if max_depth is not None and depth > max_depth:
            return []
        lines = []
        if depth == 0 :
            lines.append(self.format_metadata(node))
        for index, child in enumerate(node.children):
            is_last = index == len(node.children) - 1
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + self.format_metadata(child))
            if child.is_dir:
                extension = "    " if is_last else "│   "
                lines.extend(
                    self.format(
                        child,
                        prefix=prefix+extension,
                        depth=depth+1,
                        max_depth=max_depth
                    )
                )
        return lines
    def get_icon(self, node : TreeNode) -> str :
        if not self.show_icons:
            return ""
        if node.is_dir:
            return "📁 "
        suffix = Path(node.name).suffix.lower()
        return FILE_ICONS.get(suffix, DEFAULT_FILE_ICON)
