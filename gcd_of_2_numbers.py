x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

if x > y:
    smaller = y
else:
    smaller = x
    
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        hcf = i
print(f"The hcf of two numbers is : {hcf}")