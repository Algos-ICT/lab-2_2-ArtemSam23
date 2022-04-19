import time
from tree import BST


def main():
    inp = open("input.txt")
    out = open("output.txt", "w")
    tree = BST()
    start = time.time()
    line = inp.readline()
    while line != "":
        items = line.split()
        if items[0] == "+":
            tree.insert(int(items[1]))
        else:
            out.write(f"{tree.min(int(items[1]))}\n")
        line = inp.readline()
    end = time.time()
    print(end - start)
    inp.close()
    out.close()


if __name__ == '__main__':
    main()
