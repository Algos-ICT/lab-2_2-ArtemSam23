def read_input_file():
    with open("input.txt") as inp:
        n = int(inp.readline())
        woods = []
        for _ in range(n):
            value, left, right = map(int, inp.readline().split())
            woods.append((left, right))
    return n, woods


def output(answer: str):
    print(answer)
    with open("output.txt", "w") as out:
        out.write(answer)


def main():
    n, woods = read_input_file()
    deeps = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if woods[i][0] == 0 and woods[i][1] == 0:
            deeps[i + 1] = 1
        else:
            deeps[i + 1] = max(deeps[woods[i][0]], deeps[woods[i][1]]) + 1
    output(str(deeps[1]) if n > 0 else "0")


if __name__ == '__main__':
    main()
