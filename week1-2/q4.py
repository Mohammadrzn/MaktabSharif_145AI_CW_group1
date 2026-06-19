my_list = ["amir","ali","azim","mohammad","ahmad"]

name = input("Enter the name: ")

if name in my_list:
    print("name is in list")
else:
    print("name is not in list.")
print("name is in list") if name in my_list else print("name is not in list.")
