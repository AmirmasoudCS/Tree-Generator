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
