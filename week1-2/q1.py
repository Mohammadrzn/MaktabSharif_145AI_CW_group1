order_list = []

while True:
    input_str = input("enter your order or press x to exit: ")
    if input_str == "x":
        break

    order_list.append(input_str)


print(order_list)
print("======================")
[print(f"{i}: {order}") for i, order in enumerate(order_list, start=1)]
print("======================")
for i, order in enumerate(order_list, start=1):
    print(f"{i}: {order}")