#Multiplication table for number
n = int(input("Enter a number : "))

print(f"\nMultiplication Table for {n}:\n")

for i in range(1,11):
    print(f"{n}x{i} = {n*i}")