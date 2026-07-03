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
    lines_depth0 = [line.plain for line in formatter.format(root, max_depth=0)]

    assert any("main.py" in line for line in lines_full)
    assert any("src" in line for line in lines_depth0)       # depth 0 children still shown
    assert not any("main.py" in line for line in lines_depth0)  # depth 1 excluded

def test_format_size_bytes():
    formatter = TreeFormatter()
    assert formatter.format_size(500) == "500 B"

def test_format_size_kb():
    formatter = TreeFormatter()
    assert formatter.format_size(2048) == "2.0 KB"

def test_format_size_mb():
    formatter = TreeFormatter()
    assert formatter.format_size(5 * 1024 * 1024) == "5.0 MB"

def test_metadata_appended_when_size_present():
    node = make_node("file.txt", size=1024)
    formatter = TreeFormatter()
    text = formatter.format_metadata(node)
    assert "1.0 KB" in text.plain

def test_metadata_appended_when_modified_present():
    node = make_node("file.txt", modified=1700000000)  # any valid timestamp
    formatter = TreeFormatter()
    text = formatter.format_metadata(node)
    # format is YYYY-MM-DD HH:MM, just check the shape is present
    assert "(" in text.plain and ")" in text.plain

def test_no_metadata_when_absent():
    node = make_node("file.txt")
    formatter = TreeFormatter()
    text = formatter.format_metadata(node)
    assert "(" not in text.plain

def test_icons_off_by_default():
    node = make_node("file.py")
    formatter = TreeFormatter(show_icons=False)
    assert formatter.get_icon(node) == ""

def test_icons_on_for_folder():
    node = make_node("src", is_dir=True)
    formatter = TreeFormatter(show_icons=True)
    assert formatter.get_icon(node) == "📁 "

def test_icons_on_for_license_file():
    node = make_node("LICENSE")
    formatter = TreeFormatter(show_icons=True)
    assert formatter.get_icon(node) == "⚖️ "

def test_unknown_theme_falls_back_to_default():
    formatter = TreeFormatter(theme_name="not_a_real_theme")
    assert formatter.theme == formatter.theme  # sanity: doesn't crash
    from tree_printer.themes import THEMES
    assert formatter.theme == THEMES["default"]

def test_format_size_boundary_exactly_1024():
       formatter = TreeFormatter()
       assert formatter.format_size(1024) == "1.0 KB"