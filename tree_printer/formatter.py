from tree_printer.models import TreeNode
class TreeFormatter:
    def format(
            self,
            node : TreeNode,
            prefix : str=""
    ) -> list[str]:
        lines = []
        for index, child in enumerate(node.children):
            is_last = index == len(node.children) - 1
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + child.name)
            if child.is_dir:
                extension = "    " if is_last else "│   "
                lines.extend(
                    self.format(
                        child,
                        prefix+extension
                    )
                )
        return lines
