def read_tree() -> list[Node]:
    file = open('input.txt')
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


class Node:
    def __init__(self, key=None):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None


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
        left_is_descending = left_is_descending and root.left.key < root.key and descend(root.left,
                                                                                         left_ancestor=root.key)

    right_is_descending = True
    if root.right is not None:
        if left_ancestor is not None:
            right_is_descending = root.right.key < left_ancestor
        right_is_descending = right_is_descending and root.key <= root.right.key and descend(root.right,
                                                                                             right_ancestor=root.key)

    return left_is_descending and right_is_descending


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None
        node = self.root
        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return None

        new = Node(key)
        if parent is None:
            self.root = new
        elif key < parent.key:
            parent.left = new
        elif key > parent.key:
            parent.right = new

    def min(self, x):
        if self.root is None:
            return 0

        way = []
        node = self.root
        while True:
            way.append(node)
            if x > node.key:
                if node.right is None:
                    break
                node = node.right
            elif x < node.key:
                if node.left is None:
                    return node.key
                node = node.left
            else:
                if node.right is None:
                    break
                node = node.right
                while node.left is not None:
                    node = node.left
                return node.key
        for i in range(len(way) - 1, -1, -1):
            if way[i].key > x:
                return way[i].key
        return 0
