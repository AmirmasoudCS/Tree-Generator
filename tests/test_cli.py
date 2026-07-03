import pytest
from tree_printer.cli import build_parser

def test_default_path_is_dot():
    parser = build_parser()
    args = parser.parse_args([])
    assert args.path == "."

def test_positional_path():
    parser = build_parser()
    args = parser.parse_args(["some/folder"])
    assert args.path == "some/folder"

def test_max_depth_long_and_short_flags():
    parser = build_parser()
    assert parser.parse_args(["--max-depth", "2"]).max_depth == 2
    assert parser.parse_args(["-md", "3"]).max_depth == 3

def test_max_depth_default_none():
    parser = build_parser()
    assert parser.parse_args([]).max_depth is None

def test_show_hidden_flag():
    parser = build_parser()
    assert parser.parse_args([]).show_hidden is False
    assert parser.parse_args(["--show-hidden"]).show_hidden is True
    assert parser.parse_args(["-sh"]).show_hidden is True

def test_dirs_only_flag():
    parser = build_parser()
    assert parser.parse_args(["-do"]).dirs_only is True

def test_exclude_dirs_accepts_multiple_values():
    parser = build_parser()
    args = parser.parse_args(["--exclude-dirs", "node_modules", ".git"])
    assert args.exclude_dirs == ["node_modules", ".git"]

def test_exclude_dirs_default_none():
    parser = build_parser()
    assert parser.parse_args([]).exclude_dirs is None


