from tree import *


def read_input() -> list[Node]:
    file = open('input.txt')
    k = int(file.readline())
    tree: list[Node] = [Node() for _ in range(k)]
    for node in tree:
        value, left, right = map(int, file.readline().split())
        node.value = value
        if left != -1:
            node.left = tree[left]
        if right != -1:
            node.right = tree[right]
    return tree


if __name__ == '__main__':
    tree = read_input()
    print(*in_order(tree[0]))
    print(*pre_order(tree[0]))
    print(*post_order(tree[0]))
