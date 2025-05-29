'''n = int(input("Enter a number : "))

while(n > 0):
    lastdigit = n % 10
    print(lastdigit)
    n = n // 10'''

n = int(input("Enter a number : "))
count = 0
while(n > 0):
    lastdigit = n % 10
    count += 1
    n = n // 10
print(count)


