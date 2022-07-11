# Honestly i don't think that being able to directly implement heap is very beneficial, so i will just use the heapq 
import heapq

class Heap:
    def __init__(self):
        self.heap = []
    def print_minimum(self):
        try:
            print(self.heap[0])
        except:
            print("Error, heap is empty")
    def push_heap(self, val: int):
        heapq.heappush(self.heap, val)
    def pop_heap(self, val:int):
        self.heap.remove(val)
        heapq.heapify(self.heap)

if __name__ == '__main__':
    t = int(input())
    heap = Heap()
    for _ in range(t):
        queries = input().split(' ')
        if queries[0] == '1':
            heap.push_heap(int(queries[1]))
        elif queries[0] == '2':
            heap.pop_heap(int(queries[1]))
        else:
            heap.print_minimum()