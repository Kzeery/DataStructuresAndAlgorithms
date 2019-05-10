CAPACITY = 10
class Heap():
    def __init__(self):
        self.heap = [0]*CAPACITY
        self.heap_size = 0

    def insert(self, item):
        if CAPACITY == self.heap_size:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)
    
    def fix_up(self, index):
        parentIndex = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parentIndex]:
            self.swap(index, parentIndex)
            self.fix_up(parentIndex)
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def get_max(self):
        return self.heap[0]

    def poll(self):
        maximum = self.get_max()
        
        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1
        self.fix_down(0)

        return maximum
    
    def fix_down(self, index):
        leftIndex = 2*index + 1
        rightIndex = 2*index + 2
        largestIndex = index

        if leftIndex < self.heap_size and self.heap[leftIndex] > self.heap[largestIndex]:
            largestIndex = leftIndex
        
        if rightIndex < self.heap_size and self.heap[rightIndex] > self.heap[largestIndex]:
            largestIndex = rightIndex

        if index != largestIndex:
            self.swap(index, largestIndex)
            self.fix_down(largestIndex)

    def heap_sort(self):
        size = self.heap_size

        for i in range(size):
            maximum = self.poll()
            print(maximum)

heap = Heap()

heap.insert(10)
heap.insert(8)
heap.insert(12)
heap.insert(20)
heap.insert(-2)
heap.insert(0)
heap.insert(1)
heap.insert(321)

heap.heap_sort()