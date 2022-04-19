from collections import deque


class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


def set_parent(child, parent):
    if child is not None:
        child.parent = parent


def keep_parent(node):
    set_parent(node.left, node)
    set_parent(node.right, node)


def rotate(parent, child):
    grandparent = parent.parent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = child
        else:
            grandparent.right = child

    if parent.left == child:
        parent.left, child.right = child.right, parent
    else:
        parent.right, child.left = child.left, parent

    keep_parent(child)
    keep_parent(parent)
    child.parent = grandparent


def sum_of_tree(root, l, r):
    stack = deque()
    nums = []
    if root is None:
        return 0
    while True:
        stack.append(root)
        if root.left is None or root.key <= l:
            break
        root = root.left

    while True:
        if len(stack) != 0:
            nums.append(stack[-1].key)
            if stack[-1].right is not None and stack[-1].key <= r:
                root = stack.pop().right
            else:
                stack.pop()
                continue
            while True:
                stack.append(root)
                if root.left is None or root.key <= l:
                    break
                root = root.left
        if len(stack) == 0:
            sum_to_return = 0
            for num in nums:
                if l <= num <= r:
                    sum_to_return += num
            return sum_to_return


class SplayTree:

    def splay(self, node):
        if node.parent is None:
            return node
        parent = node.parent
        grandparent = parent.parent
        if grandparent is None:
            rotate(parent, node)
            return node
        else:
            flag = (grandparent.left == parent) == (parent.left == node)
            if flag:
                rotate(grandparent, parent)
                rotate(parent, node)
            else:
                rotate(parent, node)
                rotate(grandparent, node)
        return self.splay(node)

    def find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return self.splay(node)
        if key < node.key and node.left is not None:
            return self.find(node.left, key)
        if key > node.key and node.right is not None:
            return self.find(node.right, key)
        return self.splay(node)

    def split(self, root, key):
        if root is None:
            return None, None
        root = self.find(root, key)
        if root.key == key:
            set_parent(root.left, None)
            set_parent(root.right, None)
            return root.left, root.right
        if root.key < key:
            right, root.right = root.right, None
            set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            set_parent(left, None)
            return left, root

    def insert(self, root, key):
        left, right = self.split(root, key)
        root = Node(key, left, right)
        keep_parent(root)
        return root

    def merge(self, left, right):
        if right is None:
            return left
        if left is None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    def remove(self, root, key):
        root = self.find(root, key)
        set_parent(root.left, None)
        set_parent(root.right, None)
        return self.merge(root.left, root.right)
