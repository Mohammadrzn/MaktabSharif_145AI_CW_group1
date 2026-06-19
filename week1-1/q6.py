print("Welcome to calculator")

while True:
    try:
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
    except ValueError:
        print("Please enter a number")
        continue

    while True:
        operator = input("Please enter operator (*, /, +, -, q(quit)): ")
        match operator:
            case "*":
                print(f"The multiplication of {num1} and {num2} is {num1 * num2}")
            case "/":
                try:
                    print(f"The division of {num1} and {num2} is {num1 / num2}")
                except ZeroDivisionError:
                    print("Number can't divided by zero")
                    break
            case "+":
                print(f"The addition of {num1} and {num2} is {num1 + num2}")
            case "-":
                print(f"The subtraction of {num1} and {num2} is {num1 - num2}")
        break