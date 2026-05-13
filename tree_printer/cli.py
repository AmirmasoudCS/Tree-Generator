import argparse
from .printer import  TreePrinter
from .formatter import TreeFormatter
def run() -> None:
    parser = argparse.ArgumentParser(
        description="Generate and print directory tree structures"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to generate the tree on"
    )
    parser.add_argument(
        "--max-depth",
        "-md",
        type=int,
        default=None,
        help="Maximum directory depth that will be generated"
    )
    parser.add_argument(
        "--output",
        "-o",
        help = "Write tree output to a file instead of printing"
    )
    parser.add_argument(
        "--show-hidden",
        "-sh",
        action="store_true",
        help="Include hidden files and directories"
    )
    parser.add_argument(
        "--dirs-only",
        "-do",
        action="store_true",
        help="Show directories only"
    )
    parser.add_argument(
        "--exclude-dirs",
        "-ed",
        nargs="+",
        default=None,
        help="Exclude directories by name"
    )
    parser.add_argument(
        "--exclude-files",
        "-ef",
        nargs="+",
        default=None,
        help="Exclude files by name"
    )
    parser.add_argument(
        "--exclude-suffixes",
        "-es",
        nargs="+",
        default=None,
        help="Exclude files by suffixes"
    )
    parser.add_argument(
        "--size",
        "-s",
        action="store_true",
        help="Show file size"
    )
    parser.add_argument(
        "--modified",
        "-m",
        action="store_true",
        help="Show last modified time"
    )
    args = parser.parse_args()
    printer = TreePrinter(
                        root_path=args.path,
                        show_hidden=args.show_hidden,
                        dirs_only=args.dirs_only,
                        exclude_dirs=args.exclude_dirs,
                        exclude_files=args.exclude_files,
                        exclude_suffixes=args.exclude_suffixes,
                        show_size=args.size,
                        show_modified=args.modified
                        )
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
    