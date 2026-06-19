list1=[]
for j in range(5):
    list1.append(int(input("please enter number: ")))
max1=list1[0]
for item in list1:
    if max1 <= item:
        max1=item
print(f"maximum= {max1}")