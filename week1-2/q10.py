contacts={"Ali": "09120000000","Sara": "09130000000","Reza": "09140000000"}

while 1:
    flag = input('1.for search 2.exit')
    if flag == "2":
        break
    name = input('Who are you looking for ? ')
    print(contacts.get(name.title(),f'{name} is not in contact list'))