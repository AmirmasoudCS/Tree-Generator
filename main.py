from tree_printer import TreePrinter, TreeFormatter
def main():
    printer = TreePrinter()
    formatter = TreeFormatter()
    tree = printer.build_tree()
    lines = formatter.format(tree)
    for line in lines:
        print(line)
if __name__ == "__main__":
    main()