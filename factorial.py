# In this code we have taken a number as input and calculated its factorial 
n = int(input("Enter a number : ")) # number input
fact = 1 # taken a extra variable 

for i in range(1,n+1):# for loop to calculate the factorial
    fact = (fact * i)


print(f"The factorial of the number is {fact}")