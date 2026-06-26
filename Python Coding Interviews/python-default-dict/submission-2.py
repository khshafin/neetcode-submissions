from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:

    my_dict = defaultdict(int)

    for char in s:
        my_dict[char] +=1
    return my_dict
    # count = defaultdict(int)

    # for char in s:
    #     count[char] += 1
    # return count


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:

    my_dict = defaultdict(list)

    for sublist in nums:
        first = sublist[0]
        my_dict[first] += sublist[1:]
    return my_dict

    #     if first not in my_dict:
    #         my_dict[first] = rest_list
    #     else:
    #         my_dict[first] += rest_list

    # return my_dict
    
    


        

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
