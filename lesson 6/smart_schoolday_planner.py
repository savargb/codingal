# Smart Schoolday Planner

print("=== Smart Schoolday Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it today?(Monday - Sunday): ").strip().capitalize()
weather = input("What is the weather today? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes/no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("." * 35)

if day in ("saturday", "sunday"):
    print("Day Type - Enjoy!")
elif day == "Monday":
    print("Day Type - First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day Type - Last school day. Return library books today.")
elif day in("Tuesday", "Wednesday", "Thursday"):
    print("Day Type - Regular School Day, ):")
else:
    print("Day Type - Not recognized. Please check the spelling.")


if weather == "sunny" and homework == "yes":
    print("After school: Head to park - Do homework and once done enjoy.")
    
if weather =="rainy" or weather == "cloudy":
    print("Weather tip: Pack umbrella - It may get wet outside")
    
if not (homework == "yes"):
    print("Homework : Not Done yet - Finish it before going outside.")
    

if weather == "rainy" and not (homework == "yes"):
    print("Stay indoors and watch favorite show after you fionish your homework.")
elif weather == "sunny" and homework == "yes" and not (day in("saturday", "sunday")):
    print("Best plan: All set for a school day, you are prepared")
elif day in ("saturday", "sunday") and weather == "sunny":
    print("Best plan   : perfect weekend weather. Go outside and have some fun!")
else:
    print("Best Plan  : Take it one step at a time, You got this!")

print()
print("Plan Complete! Have a wonderful day!")
print("===============================================")