# In this code we have taken a number as input an to check whether it is even or odd we have divided the number by two

#If the number divided by two and the remainder is zero it is even else it is odd
num_1 = int(input("Enter a number : "))

if(num_1 % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")