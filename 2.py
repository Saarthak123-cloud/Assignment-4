year=int(input("Enter the year you want to check:"))
if year%4==0 and year%400==0:
    print("Given year is a leap year")
elif year%4==0 and year%100==0:
    print("Given year is not a leap year")
elif year%4==0:
    print("Its a leap year")
else:
    print("Its not a leap year")
