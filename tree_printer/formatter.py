from datetime import datetime
from rich.text import Text
from .file_types import FILE_STYLES, DEFAULT_FILE_STYLE
from .themes import THEMES
from tree_printer.models import TreeNode
from pathlib import Path
from typing import List
from .icons import FILE_ICONS, DEFAULT_FILE_ICON

class TreeFormatter:
    def __init__(
            self,
            show_icons : bool = False,
            theme_name : str = "default"
    ):
        self.show_icons = show_icons
        self.theme = THEMES.get(theme_name, THEMES["default"])
    def format_metadata(self, node : TreeNode) -> Text:
        style_key = self.get_style_key(node)
        style = self.theme.get(style_key, "white")
        label = f"{self.get_icon(node)}{node.name}"
        text = Text(label, style=style)
        metadata = []
        if node.size is not None:
            metadata.append(f"{node.size} B")
        if node.modified is not None:
            formatted_date = datetime.fromtimestamp(node.modified).strftime("%Y-%m-%d %H:%M")
            metadata.append(formatted_date)
        if metadata:
            text.append(f" ({' | '.join(metadata)})", style="dim")
        return text
    def format(
            self,
            node : TreeNode,
            prefix : str = "",
            depth : int = 0,
            max_depth : int | None = None
    ) -> list[Text]:
        if max_depth is not None and depth > max_depth:
            return []
        lines = []
        if depth == 0 :
            lines.append(self.format_metadata(node))
        for index, child in enumerate(node.children):
            is_last = index == len(node.children) - 1
            connector = "└── " if is_last else "├── "
            line = Text(prefix + connector)
            line.append(self.format_metadata(child))
            lines.append(line)
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
        name = node.name.lower()
        if name == "license":
            return "⚖️ "
        suffix = Path(node.name).suffix.lower()
        return FILE_ICONS.get(suffix, DEFAULT_FILE_ICON)
    def get_style_key(self, node : TreeNode) -> str:
        if node.is_dir:
            return "folder"
        suffix = Path(node.name).suffix.lower()
        return FILE_STYLES.get(suffix, DEFAULT_FILE_STYLE)
    
