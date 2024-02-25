age = int(input("Enter Age - "))
day = input("Enter Day - ")

price = 12 if age>=18 else 8

if day=="wednesday":
    price = price-2
    
print("Ticket Price Of The Day is : ",price,"$")