class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        if self.children:
            return f"{self.value} {' '.join(str(child) for child in self.children)}"
        else:
            return str(self.value)


# Example usage:
# Constructing a simple parse tree
root = ParseTreeNode('S')
expr = ParseTreeNode('expr')
term = ParseTreeNode('term')
num1 = ParseTreeNode('1')
op = ParseTreeNode('+')
num2 = ParseTreeNode('2')

root.add_child(expr)
expr.add_child(term)
term.add_child(num1)
term.add_child(op)
term.add_child(num2)

# Printing the parse tree
print(root)
