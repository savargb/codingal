name = input("enter your real name, agent:")
gadget = input("enter your fav gadget, agent:")

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

print("Name:",name,"-> type:",type(name))
print("Gadget:",gadget,"-> type:",type(gadget))
print("Agent Number:",agent_number,"-> type:",type(agent_number))
print("Speed Rating:",speed_rating,"-> type:",type(speed_rating))
print("Mission Count:",mission_count,"-> type:",type(mission_count))
print("Height (m):",height_m,"-> type:",type(height_m))
print("Is Active:",is_active,"-> type:",type(is_active))

agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
status_text = str(is_active)

print("Agent Number as Text:",agent_number_text,"-> type:",type(agent_number_text))
print("Speed Rating as Text:",speed_rating_text,"-> type:",type(speed_rating_text))
print("Mission Count as Text:",mission_count_text,"-> type:",type(mission_count_text))
print("Status as Text:",status_text,"-> type:",type(status_text))

first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First three letters of name:",first_three)
print("Last letter of name:",last_letter)
print("Secret Code Name:",code_name)

reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:",reversed_gadget)

badge_line_1 = "AGENT" + code_name.upper()
badge_line_2 = "ID:" + agent_number_text + " | MISIONS: " + mission_count_text
badge_line_3 = "SPEED:" + speed_rating_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()

print("")
print("=====  SECRET ADGENT BADGE  =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
