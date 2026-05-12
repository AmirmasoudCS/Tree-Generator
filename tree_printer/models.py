from dataclasses import dataclass, field
@dataclass
class TreeNode:
    name : str
    is_dir : bool
    children : list["TreeNode"] = field(default_factory=list)