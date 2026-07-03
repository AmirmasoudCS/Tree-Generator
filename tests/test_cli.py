import pytest
from tree_printer.cli import build_parser

def test_default_path_is_dot():
    parser = build_parser()
    args = parser.parse_args([])
    assert args.path == "."

