from typing import List

def count_unique_words(words: List[str]) -> int:
    if len(words) == 0:
        return 0
    else:
        my_set = set(words)
    #my_list = list(my_set)

        count = 0

        for i in range(len(my_set)):
            count += 1
        return count


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
