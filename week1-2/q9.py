phonebook = {}

while True:
    name = input('name:exit to exit ')

    if name.lower().strip() == 'exit':
        break
    phone = input('phone')

    phonebook[name] = phone

print('\nphonebook:', phonebook)