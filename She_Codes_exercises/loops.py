
# # question 1
# output_numbered_list = False
# number_list = []
# while output_numbered_list == False:
#     number = input("Enter a number: ")
#     if number == "":
#         output_numbered_list = True
#     else:
#         number_list.append(int(number))
# print(number_list)

# total = sum(number_list)
# print(total)


# # question 2

# mailing_list = [
#     ["Rory", "roary@moth.catchers"],
#     ["remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Biscuit", "biscuit@whippies.park"],
#     ["Rory", "rory@whippies.park"],
# ]

# for item in mailing_list:
#     print(f"{item[0]}: {item[1]}")


# # question 3

# counter = 0
# name_list = []
# while counter < 3:
#     name = input("Type a name: ")
#     name_list.append(name)
#     counter = counter + 1
# #print(name_list)
# for item in name_list:
#     print(item)


# question 4

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
grocery_bill = {

}

total = 0

for item in groceries:
    number_of_items = input(f"how many units of {item[0]} did you buy? ")
    total_cost_of_item = item[1] * int(number_of_items)
    grocery_bill[item[0]] = total_cost_of_item
    total = total + total_cost_of_item
    print(grocery_bill)


print("====Izzy's Food Emporium====")
for item in groceries:
    item_name = item[0]
    # print(f"{item_name:<20} ${grocery_bill[item_name]:.2f}")
print("============================")
print(f"${total:>27.2f}")

