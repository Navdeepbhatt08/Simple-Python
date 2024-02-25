marks = int(input("Enter The Marks : "))

if marks>100:
    print("Please Verify Your Marks")

if(90<=marks<=100):
    print("Your Grade : A ")

elif(80<=marks<90):
    print("Your Grade : B ")

if(70<=marks<80):
    print("Your Grade : C ")

if(60<=marks<70):
    print("Your Grade : D ")

if(50<=marks<60):
    print("Your Grade : E ")

if(40<=marks<50):
    print("Your Grade : F ")

if marks<40:
    print(" Fail ")