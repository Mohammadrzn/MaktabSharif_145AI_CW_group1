with open("name.txt", "a+") as file:
    names = input("enter the names separate by \",\" or for exit type \"exit\":")
    name_list = names.split(",")
    for name in name_list:
        if "exit" == name.lower():
            break
        file.write(f'{name.strip()}\n')