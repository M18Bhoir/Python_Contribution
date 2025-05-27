# In this we are solving a question called sum of n natural numbers
n = int(input("Enter a number : ")) # Input 
sum = 0 # initializing and declaring the sum as 0
for i in range(1,n+1): # for loop for iterating the number
    sum = i + sum # getting the sum
print(f"The sum of n natural numbers is : {sum}") 