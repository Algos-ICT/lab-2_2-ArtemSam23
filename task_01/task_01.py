if __name__ == '__main__':
    tree = read_tree()
    print(*in_order(tree[0]))
    print(*pre_order(tree[0]))
    print(*post_order(tree[0]))
