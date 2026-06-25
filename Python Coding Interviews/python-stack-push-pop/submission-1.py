from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reversed_list = []

    for i in range(len(arr)):
        removed_int = arr.pop()
        reversed_list.append(removed_int)
    return reversed_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
