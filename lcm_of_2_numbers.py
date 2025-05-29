x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

if x > y:
    smaller = y
else:
    smaller = x
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
       hcf = i
lcm = (x*y)/hcf
print(f"The lcm of 2 numbers is : {lcm}")