n = int(input("Enter a number: "))
x = 0
y = 1
for i in range(n):
    print(x)
    temp = x
    x = y
    y = temp + y
