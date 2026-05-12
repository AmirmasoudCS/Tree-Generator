import argparse
from .printer import  TreePrinter
from .formatter import TreeFormatter
def run():
    parser = argparse.ArgumentParser(
        description="========== Print a directory tree =========="
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to generate the tree on"
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum directory depth that will be generated"
    )
    args = parser.parse_args()
    printer = TreePrinter(root_path=args.path)
    formatter = TreeFormatter()
    tree = printer.build_tree()
    lines = formatter.format(tree, max_depth=args.max_depth)
    for line in lines:
        print(line)