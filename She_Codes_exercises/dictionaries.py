

groceries = {
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
}
    
grocery_bill = {}

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
    print(f"{item_name:<20} ${grocery_bill[item_name]:.2f}")
print("============================")
print(f"${total:>27.2f}")








#exercise 2
# import pprint

# names = [
#     "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
#     "Joy", "Katie", "Maddie", "Tash", "Nic",
#     "Rachael", "Bec", "Bec", "Tabitha", "Teagan",
#     "Viv", "Anna", "Catherine", "Catherine", "Debby",
#     "Gab", "Megan", "Michelle", "Nic", "Roxy",
#     "Samara", "Sasha", "Sohpie", "Teagen", "Viv"
# ]

# count = {}

# for individual_name in names:
#     count.setdefault(individual_name, 0)
#     count[individual_name] = count[individual_name] + 1
# pprint.pprint(count)
