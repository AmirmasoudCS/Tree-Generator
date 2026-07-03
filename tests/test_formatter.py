from tree_printer.models import TreeNode
from tree_printer.formatter import TreeFormatter

def make_node(name, is_dir=False, children=None, size=None, modified=None):
    return TreeNode(
        name=name,
        is_dir=is_dir,
        children=children or [],
        size=size,
        modified=modified,
    )

def test_format_lists_root_and_children():
    root = make_node("project", is_dir=True, children=[
        make_node("main.py"),
        make_node("README.md"),
    ])

    formatter = TreeFormatter()
    lines = [line.plain for line in formatter.format(root)]

    # root line + 2 children
    assert any("project" in line for line in lines)
    assert any("main.py" in line for line in lines)
    assert any("README.md" in line for line in lines)

def test_last_child_uses_corner_connector():
    root = make_node("project", is_dir=True, children=[
        make_node("a.py"),
        make_node("b.py"),  # last
    ])

    formatter = TreeFormatter()
    lines = [line.plain for line in formatter.format(root)]

    b_line = next(l for l in lines if "b.py" in l)
    a_line = next(l for l in lines if "a.py" in l)

    assert b_line.startswith("└── ")
    assert a_line.startswith("├── ")

def test_nested_dir_gets_indented_prefix():
    root = make_node("project", is_dir=True, children=[
        make_node("src", is_dir=True, children=[
            make_node("main.py"),
        ]),
    ])

    formatter = TreeFormatter()
    lines = [line.plain for line in formatter.format(root)]

    main_line = next(l for l in lines if "main.py" in l)
    # src is the only (last) child, so extension is "    " not "│   "
    assert main_line.startswith("    └── ")

def test_max_depth_limits_output():
    root = make_node("project", is_dir=True, children=[
        make_node("src", is_dir=True, children=[
            make_node("main.py"),
        ]),
    ])

    formatter = TreeFormatter()
    lines_full = [line.plain for line in formatter.format(root)]
    lines_limited = [line.plain for line in formatter.format(root, max_depth=1)]

    assert any("main.py" in line for line in lines_full)
    assert not any("main.py" in line for line in lines_limited)

def test_format_size_bytes():
    formatter = TreeFormatter()
    assert formatter.format_size(500) == "500 B"

def test_format_size_kb():
    formatter = TreeFormatter()
    assert formatter.format_size(2048) == "2.0 KB"

def test_format_size_mb():
    formatter = TreeFormatter()
    assert formatter.format_size(5 * 1024 * 1024) == "5.0 MB"