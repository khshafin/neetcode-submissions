from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in range(len(arr2)):
        elem_to_add = arr2[i]

        arr1.append(elem_to_add)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:

    empty_list = []

    if n > len(arr):
        return empty_list
    i = 0
    while i < len(range(n)):
        arr.pop()
        i += 1
    return arr



def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if index > len(arr):
        arr.append(element)
    else:
        arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
