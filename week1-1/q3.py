num_1 = int(input("Enter first number please : "))
num_2 = int(input("Enter second number please : "))

if num_1 > num_2 :
    print(num_1 , "is bigger than" , num_2)
    print(f"{num_1} is bigger than {num_2}")
elif num_1 < num_2 :
    print(num_1 , "is smaller than" , num_2)
else :
    print(num_1 , "is draw with" , num_2)