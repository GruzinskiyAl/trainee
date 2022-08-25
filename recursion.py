# Write a function sorted_print(node: Node) that recursively prints the labels
# of all nodes in the subtree rooted at node in ascending sorted order.
# For example, if we had a tree with some root node root, then calling sorted_print(root)
# would print the labels of all nodes in the tree in ascending sorted order.
# Print a single label per line. You can assume that the Binary Search Tree structure
# is valid (i.e., all nodes are larger than all of their descendants in their
# left subtree and smaller than all of their descendants in their right subtree).
import io
import sys


# Sample Input:

# Cherry -> Apple
# Cherry -> Lemon
# Lemon -> Imbe
# Lemon -> Nectarine
# Nectarine -> Mango
# ---------------------
# Sample Output:
#
# Apple
# Cherry
# Imbe
# Lemon
# Mango
# Nectarine


class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.parent = None
        self.leftChild = left
        self.rightChild = right
        if left:
            left.parent = self
        if right:
            right.parent = self


def sorted_print(node):
    pass


def test():
    apple = Node("Apple")
    mango = Node("Mango")
    nectarine = Node("Nectarine", mango)
    imbe = Node("Imbe")
    lemon = Node("Lemon", imbe, nectarine)
    cherry = Node("Cherry", apple, lemon)

    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sorted_print(cherry)
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue() == "Apple\nCherry\nImbe\nLemon\nMango\nNectarine\n"
    ), "Answer is invalid"


test()
