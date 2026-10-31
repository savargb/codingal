temperature = int(input("Enter today's temperature in celsius"))

if temperature < 20:
    outfit = "Jacket"
    print("It is cold today")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today")
    print("wear a ", outfit)
    
is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Bring and umbrella")
    
wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    need_windbreaker = "yes"
    print("it is windy today. ")
    print("Wear a windbreaker over your", outfit)
else:
    need_windbreaker = "no"
    print("It is calm today")
    print("No windbreaker needed over your", outfit)
    
has_puddles = input("Are there puddles on the ground?")

if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet. ")
    print("wear", shoes)
    
print("")
print("Weather check complete")

print("====== WEATHER OUTFIT PICKER ======")
print("Temperature : ", temperature)
print("Outfit Chosen: ", outfit)
print("Raining :", is_raining)
print("Windbreaker needed: ", need_windbreaker)
print("Shoes Chosen:", shoes)
print("====================================")



    

    
    