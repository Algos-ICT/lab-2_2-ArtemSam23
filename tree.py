class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def in_order(root: Node):
    if root:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)


def pre_order(root: Node):
    if root:
        yield root.value
        yield from pre_order(root.left)
        yield from pre_order(root.right)


def post_order(root: Node):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.value
