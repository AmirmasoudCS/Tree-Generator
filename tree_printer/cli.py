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
    parser.add_argument(
        "--output",
        "-o",
        help = "Write tree output to a file instead of printing"
    )
    args = parser.parse_args()
    printer = TreePrinter(root_path=args.path)
    formatter = TreeFormatter()
    tree = printer.build_tree()
    lines = formatter.format(tree, max_depth=args.max_depth)
    output = "\n".join(lines)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(output)
        print(f"Tree written into {args.output}")
    else:
        print(output)
    