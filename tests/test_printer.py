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

def test_dirs_only_excludes_files(tmp_path):
    (tmp_path / "folder").mkdir()
    (tmp_path / "file.txt").write_text("")

    printer = TreePrinter(root_path=tmp_path, dirs_only=True)
    root = printer.build_tree()

    names = [c.name for c in root.children]
    assert "folder" in names
    assert "file.txt" not in names

def test_show_hidden_false_by_default(tmp_path):
    (tmp_path / ".secret").write_text("")
    (tmp_path / "visible.txt").write_text("")

    printer = TreePrinter(root_path=tmp_path)
    root = printer.build_tree()

    names = [c.name for c in root.children]
    assert ".secret" not in names
    assert "visible.txt" in names

def test_show_hidden_true_includes_dotfiles(tmp_path):
    (tmp_path / ".secret").write_text("")

    printer = TreePrinter(root_path=tmp_path, show_hidden=True)
    root = printer.build_tree()

    names = [c.name for c in root.children]
    assert ".secret" in names

def test_exclude_dirs(tmp_path):
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "app.py").write_text("")

    printer = TreePrinter(root_path=tmp_path, exclude_dirs=["node_modules"])
    root = printer.build_tree()

    names = [c.name for c in root.children]
    assert "node_modules" not in names
    assert "app.py" in names

def test_gitignore_respected(tmp_path):
    (tmp_path / ".gitignore").write_text("*.log\n")
    (tmp_path / "debug.log").write_text("")
    (tmp_path / "main.py").write_text("")

    printer = TreePrinter(root_path=tmp_path, use_gitignore=True)
    root = printer.build_tree()

    names = [c.name for c in root.children]
    assert "debug.log" not in names
    assert "main.py" in names

def test_no_gitignore_file_does_not_crash(tmp_path):
    printer = TreePrinter(root_path=tmp_path, use_gitignore=True)
    assert printer.gitignore_spec is None

def test_sort_by_name(tmp_path):
    (tmp_path / "b.txt").write_text("")
    (tmp_path / "a.txt").write_text("")
    (tmp_path / "folder").mkdir()

    printer = TreePrinter(root_path=tmp_path, sort_by="name")
    items = printer.get_items(tmp_path)
    names = [p.name for p in items]

    assert names == ["folder", "a.txt", "b.txt"]

def test_sort_by_size(tmp_path):
    (tmp_path / "small.txt").write_text("a")
    (tmp_path / "big.txt").write_text("a" * 100)

    printer = TreePrinter(root_path=tmp_path, sort_by="size")
    items = printer.get_items(tmp_path)
    names = [p.name for p in items]

    assert names == ["big.txt", "small.txt"] 