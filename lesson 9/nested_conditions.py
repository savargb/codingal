print("==============================")
print("  Welcome to ride builder!")
print("==============================")
print()

print("Step 1: Pick your vehicle:")
print("Bike - 1")
print("Car - 2")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Choos your Bike Type")
    print(" Scooty - 1")
    print(" Mountain Bike - 2")
    print()
    
    bike_type = int(input("Enter 1 or 2: "))
    print()
    
    if bike_type == 1:
        print(" You Picked Scooty")
        print("Top Speed: 80 Km/h")
        print("Best For : City Roads")
    else:
        print(" You Picked Mountain Bike")
        print("Top Speed : 80KM/h")
        print(" Best For : Offroad Trails")

elif choice == 2:
    print("Step 2: Choos your Bike Type")
    print(" Sedan - 1")
    print(" SUV - 2")
    print()
    
    car_type = int(input("enter 1 or 2"))
    print()
    
    if car_type == 1:
        print(" You Picked SUV")
        print("Top Speed: 80 Km/h")
        print("Best For : City Roads")
        print("7 Passengers")
    else:
        print(" You Picked Sedan")
        print("Top Speed : 80KM/h")
        print(" Best For : Offroad Trails")
        print("Best for: Off-Road Adventurers")
else:
    print("Invalid Choice")
    print("Please Enter 1 for Bike and 2 for Car")
    
print()
print("==================================")
print("Your Custom Ride is ready!")
        

