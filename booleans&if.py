# question 1
moths_in_house = True

if moths_in_house:
    print("Get the moths!")

else:
    print("No threats detected")

# question 2
moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
if not moths_in_house and not mitch_is_home:
    print("No threats detected")
if moths_in_house and not mitch_is_home:
    print("Meooooooooooow! Hissssss!")
if not moths_in_house and mitch_is_home:
    print("Climb on Mitch")

# question 3
light_colour_is_red = False
light_colour_is_green = True
light_colour_is_amber = True
car_detected = True

if light_colour_is_red and not car_detected:
    print("Do nothing")
if light_colour_is_red and car_detected:
    print("Flash!")
if light_colour_is_green and not car_detected:
    print("Do nothing")
if light_colour_is_green and car_detected:
    print("Do nothing")
if light_colour_is_amber and not car_detected:
    print("Do nothing") 
if light_colour_is_amber and car_detected:
    print("Do nothing") 

# question 4
height_promtp = input("what is your height in cms?")

height_promtp < 120 = True

if height_promtp:
    print("Hop on!")
else:
    print("Sorry, not today :(")

