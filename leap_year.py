# In this code we have calculated a leap year
year = int(input("Enter year : "))

# The condition for leap year is it shuold be divisible by four. Or it should be divisibe by four and divisible by 400
if(year % 4 == 0 or year % 100 == 0 and year % 400 == 0 ):
    print("It is leap year ")
else:
    print("It is not a leap year")