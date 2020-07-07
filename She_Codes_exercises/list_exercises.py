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
    ["Rory", "roary@moth.catchers"],
    ["remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")


# question 3

counter = 0
name_list = []
while counter < 3:
    name = input("Type a name ")
    name_list.append(name)
    counter = counter + 1
#print(name_list)
for item in name_list:
    print(item)

#question 4

user_string = input("Enter a String")
list(user_string)



