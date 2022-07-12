from heapq import heapify, heappush

# cannot solve, i got it from the discussion

def solve(arr, queries):
    results = []
    for d in queries:
        result = 10 ** 6
        heap = [-i for i in arr[0:d]]
        heapify(heap)
        result = min(result, -heap[0])
        for i in range(1, len(arr) - d + 1):
            if arr[i - 1] == -heap[0]:
                heap = [-i for i in arr[i: i + d]]
                heapify(heap)
            else:
                heappush(heap, -arr[i + d - 1])
            result = min(result, -heap[0])
        results.append(result)
    return results