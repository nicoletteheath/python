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

for cat_name in mailing_list:
    print(f"{mailing_list[0]} cats:")
    for cat in mailing_list[1:]:
        print(f"    {cat}")


