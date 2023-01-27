x= int(input("If candy is divided  among 5 people, how many pieces left over?"))
y = int(input("If candy is divided  among 6 people, how many pieces left over?"))
z= int(input("If candy is divided  among 7 people, how many pieces left over?"))

if x> 5 or y> 6 or z> 7:
   print("Are jou joking me?")
candy_found = False
for i in range(1,201):
    if i%5 == x and i%6==y and i%7==z:
        print(i)
        candy_found = True
if(not candy_found):print("No such number less than 200 exists")