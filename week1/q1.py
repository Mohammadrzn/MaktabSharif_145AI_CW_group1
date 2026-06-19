# input
while 1:
    try:
        age = int(input('enter your age: '))
        name = input('enter your name: ')
        break
    except:
        print('Enter digit for age')
        continue


# output
print(f"Hello {name},you are {age}")
