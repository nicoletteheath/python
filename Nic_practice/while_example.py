spam = 0
while spam < 5:
    print("Hello World")
    spam = spam + 1

name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
print("Thank you")

name = ""
while True: #this will always be true
    print("Please type your name.")
    name = input()
    if name == "your name": #the if statement is used to break out of the loop
        break   #the break is what actually breaks out of the loop 
print("Thank you")