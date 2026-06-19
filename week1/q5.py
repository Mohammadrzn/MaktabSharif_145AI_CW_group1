num = 0
while 1:
    try:
        num = int(input("enter your number: "))
        break
    except ValueError as e:
        print(e)
        continue
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")