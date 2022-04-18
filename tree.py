class Node:
    def __init__(self, key=None):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None


def read_tree() -> list[Node]:
    file = open('task_17/input.txt')
    k = int(file.readline())
    tree: list[Node] = [Node() for _ in range(k)]
    for node in tree:
        key, left, right = map(int, file.readline().split())
        node.key = key
        if left != -1:
            node.left = tree[left]
        if right != -1:
            node.right = tree[right]
    return tree


def in_order(root: Node):
    if root:
        yield from in_order(root.left)
        yield root.key
        yield from in_order(root.right)


def pre_order(root: Node):
    if root:
        yield root.key
        yield from pre_order(root.left)
        yield from pre_order(root.right)


def post_order(root: Node):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.key


def descend(root: Node, left_ancestor=None, right_ancestor=None) -> bool:
    left_is_descending = True
    if root.left is not None:
        if right_ancestor is not None:
            left_is_descending = root.left.key > right_ancestor
        left_is_descending = left_is_descending and root.left.key < root.key and descend(root.left, left_ancestor=root.key)

    right_is_descending = True
    if root.right is not None:
        if left_ancestor is not None:
            right_is_descending = root.right.key < left_ancestor
        right_is_descending = right_is_descending and root.key <= root.right.key and descend(root.right, right_ancestor=root.key)

    return left_is_descending and right_is_descending
