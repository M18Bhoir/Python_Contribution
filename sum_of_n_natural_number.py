n = int(input("Enter a number : "))
sum = 0
for i in range(1,n+1):
    sum = i + sum
print(f"The sum of n natural numbers is : {sum}")