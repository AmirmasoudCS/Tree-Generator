from tree_printer.printer import TreePrinter

def test_build_tree_basic_structure(tmp_path):
    # Building a small fake project
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("print('hi')")
    (tmp_path / "README.md").write_text('# hello')
    # Making actions
    printer = TreePrinter(root_path=tmp_path)
    root = printer.build_tree()
    # Asserting
    names = [child.name for child in root.children]
    assert "src" in names
    assert "README.md" in names

    src_node = next(c for c in root.children if root.children == "src")
    assert src_node.is_dir is True
    assert any(c.name=="main.py" for c in src_node.children)