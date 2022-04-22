class MaxHeap:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def heapify(self, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < self.size and self.heap_list[left_child] > self.heap_list[largest]:
            self.heap_list[largest], self.heap_list[left_child] = self.heap_list[left_child], self.heap_list[largest]
            self.heapify(left_child)

        if right_child < self.size and self.heap_list[right_child] > self.heap_list[largest]:
            self.heap_list[largest], self.heap_list[right_child] = self.heap_list[right_child], self.heap_list[largest]
            self.heapify(right_child)

    def build_heap(self, l: list):
        self.heap_list = l
        self.size = len(l)
        for i in range(len(l) // 2, -1, -1):
            self.heapify(i)

    def add(self, x):
        self.heap_list.append(x)
        self.size = len(self.heap_list)
        index = self.size - 1
        parent = (index-1) // 2

        while parent >= 0 and index > 0:
            if x > self.heap_list[parent]:
                self.heap_list[index], self.heap_list[parent] = self.heap_list[parent], self.heap_list[index]
            index = parent
            parent = (index-1) // 2

    def index(self, x):
        if x == self.heap_list[0]:
            return 0
        for i in range(self.size//2):
            if x == self.heap_list[2*i + 1]:
                return 2*i + 1
            if x == self.heap_list[2*i + 2]:
                return 2*i + 2
        return -1

    def remove(self, index):
        self.heap_list[index], self.heap_list[-1] = self.heap_list[-1], self.heap_list[index]
        element = self.heap_list.pop(-1)
        self.size = len(self.heap_list)
        self.heapify(0)
        return element

    def find_n_max(self, n):
        from heapq import nlargest
        return nlargest(n, self.heap_list)[-1]
