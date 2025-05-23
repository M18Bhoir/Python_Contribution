# In this code we have taken three number as input a,b and c 
# In this code we have make a comparison in the numbers that which number is greater
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if(a>=b and a>=c):
    largest = a
elif (b>=a and b>=c):
    largest = b
else:
    largest = c

print(f"The largest number is : {largest} ")