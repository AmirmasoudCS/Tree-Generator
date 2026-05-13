from datetime import datetime
from tree_printer.models import TreeNode
class TreeFormatter:
    def format_metadata(self, node : TreeNode) -> str:
        metadata = []
        if node.size is not None:
            metadata.append(f"{node.size} B")
        if node.modified is not None:
            formatted_date = datetime.fromtimestamp(node.modified).strftime("%Y-%m-%d %H:%M")
            metadata.append(formatted_date)
        if metadata:
            return f"{node.name} ({' | '.join(metadata)})"
        return node.name
    def format(
            self,
            node : TreeNode,
            prefix : str="",
            depth : int = 0,
            max_depth : int | None = None
    ) -> list[str]:
        if max_depth is not None and depth > max_depth:
            return []
        lines = []
        if depth == 0 :
            lines.append(node.name)
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
