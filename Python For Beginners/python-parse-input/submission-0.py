from typing import List

def read_integers() -> List[int]:
    user_input_list = []
    user_input = input()
    user_input_list_init = user_input.split(",")
    for i in user_input_list_init:
        i = int(i)
        user_input_list.append(i)
    #user_input_list = user_input.split(",")
    return user_input_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
