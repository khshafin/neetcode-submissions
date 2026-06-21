from typing import List # this is used to add type hints for List type

# def get_sum(nums: List[int]) -> int:
#     running_sum = 0
#     for i in nums:
#         running_sum += i
#     return running_sum

def get_sum(nums: List[int]) -> int:
    running_sum = 0
    for i in range(len(nums)):
        value = nums[i]
        running_sum += value
    return running_sum

def get_min(nums: List[int]) -> int:
    running_min = nums[0]
    for i in range(len(nums)):
        if nums[i] < running_min:
            running_min = nums[i]
    return running_min

def get_max(nums: List[int]) -> int:
    running_max = nums[0]
    for i in range(len(nums)):
        if nums[i] > running_max:
            running_max = nums[i]
    return running_max
    

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
