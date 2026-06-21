your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}
print(your_dict)
print(your_dict["a"])
#print("d" in your_dict)
if "d" in your_dict:
    print(True)
else:
    print(False)
your_dict["a"] = 4
print(your_dict)
