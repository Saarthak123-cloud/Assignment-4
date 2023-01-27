score=int(input("Enter your marks"))
if score>80:
    print("You scored A grade")
elif 60<=score<80:
    print("You scored B grade")
elif 50<=score<60:
    print("You scored C grade")
elif 45<=score<50:
    print("You scored D grade")
elif 25<=score<45:
    print("You scored E grade")
elif score<25:
    print("You scored F grade")