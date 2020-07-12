

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total = 0

for item in groceries:
    number_of_items = input(f"how many units of {item[0]} did you buy? ")
    total_cost_of_item = item[1] * int(number_of_items)
    print(total_cost_of_item)
    total = total + total_cost_of_item

total = f"${total:.2f}"

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<20} ${total_cost_of_item:.2f}")
print("============================")
print(f"{total:>27}")
