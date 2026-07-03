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

