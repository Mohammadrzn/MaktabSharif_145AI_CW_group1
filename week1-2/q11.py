# variable
phone_book = {}

# loop
while 1:
    flag = input('1. Add 2.search 3.show 4.exit')
    if flag == "4":
        # exit
        break
    elif flag == "1":
        #add
        name = input('Enter name: ')
        phone_number = input('Enter phone number: ')
        phone_book[name] = phone_number
    elif flag == "2":
        # search
        name = input('Enter name: ')
        print(phone_book.get(name.lower(),f'{name} is not in contact list'))

    elif flag == "3":
        #show
        for people,number in zip(phone_book.keys(),phone_book.values()):
            print(f"{people} -- {number}",end='\n')