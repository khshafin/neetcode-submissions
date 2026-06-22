from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    if 7 not in nums:
        return -1
    for i, number in enumerate(nums):
        if number == 7:
            return i

    
        
        

        
           


def get_dist_between_sevens(nums: List[int]) -> int:
    index_list = []
    for i, number in enumerate(nums):
        if number == 7:
            index_list.append(i)
    #return index_list
    index_first_two = index_list[:2]
    
    return index_first_two[1] - index_first_two[0]


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
