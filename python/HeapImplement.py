class Heap:
    def __init__(self, comparator):
        self.arr = []
        self.comparator = comparator

    def get_parent(self, k):
        return (k - 1) // 2

    def peek(self):
        return self.arr[0]

    def push(self, v):
        self.arr.append(v)
        self._heapify_up(len(self.arr) - 1)

    def pop(self):
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, k):
        parent = self.get_parent(k)
        if parent == -1:
            return
        if not self.comparator(self.arr[parent], self.arr[k]):
            self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent]
            self._heapify_up(parent)

    def _heapify_down(self, k):
        if k >= len(self.arr):
            return
        left = 2 * k + 1
        right = 2 * k + 2
        index = k
        if left < len(self.arr) and not self.comparator(self.arr[index], self.arr[left]):
            index = left
        if right < len(self.arr) and not self.comparator(self.arr[index], self.arr[right]):
            index = right
        if index != k:
            self.arr[index], self.arr[k] = self.arr[k], self.arr[index]
            self._heapify_down(index)

    def make_heap(self, arr):
        for _, v in enumerate(arr):
            self.arr.append(v)

        index = (len(self.arr) - 1) // 2
        for i in range(index, -1, -1):
            self._heapify_down(i)


# We can use it to construct min heap and max heap as below:

min_heap = Heap(lambda a, b : a < b)
max_heap = Heap(lambda a, b : a > b)

arr = [4, 3, 5, 2, 1, 6, 8, 7, 9]
min_heap.make_heap(arr)
max_heap.make_heap(arr)
# print(min_heap)
# print(max_heap)

print(min_heap.peek())
# 1
print(max_heap.peek())
# 9
min_heap.push(0)
max_heap.push(10)

print(min_heap.peek())
# 0
print(max_heap.peek())
# 10

min_heap.pop()
max_heap.pop()

print(min_heap.peek())
#2
print(max_heap.peek())
#8