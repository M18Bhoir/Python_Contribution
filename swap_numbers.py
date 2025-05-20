# In this code we have swapped two numbers using a third variable temp
a = int(input("Enter a : "))
b = int(input("Enter b : "))
temp = 0
print(f"The numbers before swap are {a} and {b}")
temp = b
b = a
a = temp
print(f"The numbers after swap are {a} and {b}")
