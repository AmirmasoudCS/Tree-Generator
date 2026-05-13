from dataclasses import dataclass, field
@dataclass
class TreeNode:
    name : str
    is_dir : bool
    size : int | None = None
    modified : float | None = None
    children : list["TreeNode"] = field(default_factory=list)