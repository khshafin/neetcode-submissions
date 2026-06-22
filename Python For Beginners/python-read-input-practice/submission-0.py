def add_two_numbers() -> int:
    user_input = input()
    user_input_split = user_input.split(",")
    my_list = []
    for i in user_input_split:
        i = int(i)
        my_list.append(i)
    running_sum = 0
    for i in my_list:
        running_sum += i
    return running_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
