import random

while True:
    number1=random.randint(1, 10)
    number2=int(input("please enter your number: "))

    if number1==number2:
        print("you won!")
    else:
        print(number1)
    flag=input("f for finish , c for continue")
    if flag=="f":
        break