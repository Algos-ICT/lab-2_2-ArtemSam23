from heap import MaxHeap


def input_file():
    with open('task_17/input.txt', 'r') as input_file:
        n = int(input_file.readline())
        for line in input_file:
            yield map(int, line.split())


def main():
    heap = MaxHeap()
    with open('task_17/output.txt', 'w') as output:
        for operator, key in input_file():
            if operator == 1:
                heap.add(key)
            elif operator == 0:
                print(heap.find_n_max(key), file=output)
            elif operator == -1:
                heap.remove(heap.index(key))


if __name__ == '__main__':
    main()
