#question 1

foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry", ["carrot", "cauliflower", "pumpkin"], "passionfruit", "mango", "kiwifruit"]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[7:11]) #treat everything in the list within a list as one item
print(foods[6][-1])

# question 2

mailing_list = [
    ["Rory", "roary@moth.catchers"]
]

#how do you get data out of a loop

my_list = []

while len(my_list) < 5:
    my_var = input("give me a number")
    my_list.append(my_var)

print(my_list)
