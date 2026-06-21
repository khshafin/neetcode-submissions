def concatenate(s1: str, s2: str) -> str:
    concatenated_str = s1 + s2
    if len(concatenated_str) <= 10:
        return concatenated_str
    else:
        return("Too long!")




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
