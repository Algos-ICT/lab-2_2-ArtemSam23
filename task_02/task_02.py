from math import inf


def read_input_file():
    with open("input.txt") as input_file:
        n, height = input_file.readline().split()
        n = int(n)
        height = float(height)
        return n, height


def output(result):
    print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)


def equal(a, b):
    return abs(a-b) <= 0.1 ** 10


def less(a, b):
    return a < b and not equal(a, b)


def more(a, b):
    return a > b and not equal(a, b)


def main():
    n, height = read_input_file()
    heights = [0] * n
    heights[0] = height
    res = inf
    left, right = 0, heights[0]
    while less(left, right):
        heights[1] = (left + right)/2
        heights[-1] = 0
        flag = False
        for i in range(2, n):
            heights[i] = 2 * heights[i-1] - heights[i-2] + 2
            if not more(heights[i], 0):
                flag = True
                break
        if more(heights[-1], 0):
            res = min(res, heights[-1])
        if flag:
            left = heights[1]
        else:
            right = heights[1]

    output(("%.6f" % res))


if __name__ == '__main__':
    main()
