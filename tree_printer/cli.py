import argparse
#from rich_argparse import RichHelpFormatter
from importlib.metadata import version
from rich.console import Console
from .themes import THEMES
__version__ = version("tree-printer")
from .printer import  TreePrinter
from .formatter import TreeFormatter


def build_parser() -> argparse.ArgumentParser:
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
    parser.add_argument(
        "--icons",
        "-i",
        action="store_true",
        help="Show icons next to files and directories"
    )
    parser.add_argument(
        "--sort",
        "-st",
        choices=["name", "size", "modified"],
        default = "name",
        help = "Sort files by name, size or modified date"
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"tree-printer {__version__}"
    )
    parser.add_argument(
        "--theme",
        "-th",
        default="default",
        choices=THEMES.keys(),
        help = "Choose the color theme"
    )
    parser.add_argument(
        "--no-color",
        "-nc",
        action="store_true",
        help="Disable colored output"
    )
    parser.add_argument(
        "--gitignore",
        "-gi",
        action="store_true",
        help="Respect .gitignore file patterns"
    )
    return parser


def run(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    printer = TreePrinter(
                        root_path=args.path,
                        show_hidden=args.show_hidden,
                        dirs_only=args.dirs_only,
                        exclude_dirs=args.exclude_dirs,
                        exclude_files=args.exclude_files,
                        exclude_suffixes=args.exclude_suffixes,
                        show_size=args.size,
                        show_modified=args.modified,
                        sort_by=args.sort,
                        use_gitignore=args.gitignore
                        )
    formatter = TreeFormatter(show_icons=args.icons, theme_name=args.theme)
    tree = printer.build_tree()
    lines = formatter.format(tree, max_depth=args.max_depth)
    if args.output:
        text_lines = [line.plain for line in lines]
        with open(args.output, "w", encoding="utf-8") as file:
            file.write("\n".join(text_lines))
        print(f"Tree written into {args.output}")
    else:
        console = Console(no_color=args.no_color)
        for line in lines:
            console.print(line)