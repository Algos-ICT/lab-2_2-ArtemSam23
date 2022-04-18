from task_16.task_16 import read_tree, descend


def output(result):
    print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)


def main():
    tree = read_tree()
    if descend(tree[0]):
        output('CORRECT')
    else:
        output('INCORRECT')


if __name__ == '__main__':
    main()
