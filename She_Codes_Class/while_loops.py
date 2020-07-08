#run a block of code until a conditon is met

counter = 10

# while counter > 0:
#     #print(counter)
#     if counter%2 ==0: #%2 if divisible by 2
#         print(f"{counter} is an even number.")
#     else:
#         print(f"{counter} is an odd number.")
#     counter = counter - 1 # as long as counter is greater than 0 keep going, will do 10, remove 1, loop back until 0 or less

# counter = 0
# while counter < 3:
#     name = input("What is your name? ")
#     counter = counter + 1

name = input("What is your name? ")
while len(name) > 1:
    if name == "Hayley":
        print("You are awesome!")
    else:
        print(f"Hi {name}")
    name = input("What is your name? ")

while True:
    name = input("What is your name? ")

