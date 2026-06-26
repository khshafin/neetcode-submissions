import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []

    reversed_heap = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)

    for i in range(len(heap)):
        popped_pair = heapq.heappop(heap)
        popped_element = popped_pair[1]
        reversed_heap.append(popped_element)
    return reversed_heap




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
