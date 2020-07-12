
# question 1
output_numbered_list = False
number_list = []
while output_numbered_list == False:
    number = input("Enter a number: ")
    if number == "":
        output_numbered_list = True
    else:
        number_list.append(int(number))
print(number_list)

total = sum(number_list)
print(total)


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
    name = input("Type a name: ")
    name_list.append(name)
    counter = counter + 1
#print(name_list)
for item in name_list:
    print(item)


# question 4


groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

for item in groceries:
    print(item)
    number_of_items = input("how many units of this item did you buy? ")
    groceries.append(number_of_items)



