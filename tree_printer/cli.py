import argparse
from .printer import  TreePrinter
from .formatter import TreeFormatter
def run():
    parser = argparse.ArgumentParser(
        description="Print a directory tree"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory"
    )
    args = parser.parse_args()
    printer = TreePrinter(root_path=args.path)
    formatter = TreeFormatter()
    tree = printer.build_tree()
    lines = formatter.format(tree)
    for line in lines:
        print(line)