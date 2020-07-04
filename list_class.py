# print("lists yay!")

# tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]

# print(tea_collection)

# print(tea_collection[0])
# print(tea_collection[3])
# print(tea_collection[0:2])
# print(tea_collection[2:4])

# print(tea_collection[-1]) #will work from back of list
# print(tea_collection[-2])
# print(tea_collection[1:-1])
# print(tea_collection[-3:-1]) #won't include the number at the end it's exclusive use [-3:] to get all the way to the end

# tea_collection[-1] = "Melbourne Breakfast" #will swap out number in the list for new item
# print(tea_collection)

# print()

# print(len(tea_collection)) # use to see (length) number of items in list could also use print(length_of_list)
# tea_collection.append("Chai") #can add items to list
# print(tea_collection)
# print(len(tea_collection))

# tea_collection.extend(["New York Breakfast", "Berry"]) #adding multiple items to list at once
# print(tea_collection)

# print()

# print(tea_collection.pop()) #to delete items. If leave blank automatically removes last from list
# print(tea_collection)

# print(tea_collection.pop(1)) #delete based on item number in bracket
# print(tea_collection)

# tea_collection.remove("Chai")
# print(tea_collection)

# del tea_collection[1:3] #to delete multiple items
# print(tea_collection)

# tea_collection.clear()
# print(tea_collection)

tea_collection = [
    ["Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Peppermint", "Lemon and Ginger", "Strawberry Cream"]
]
print(tea_collection)
print(tea_collection[0]) #item in first list
print(tea_collection[0][0]) #index the parent list, second one indexes that particular item

black_teas = tea_collection[0] #same outcome as above but more work
print(black_teas[0]) 

tea_collection.append(["Chamomile", "Green", "Dandelion"])
print(tea_collection)

print(len(tea_collection))

if len(tea_collection) > 3:
    print("greater than3")
else:
    print("less than or equal to 3")

black_teas = tea_collection[0]
print(black_teas)

if "Chai" in black_teas:
    print("Yay! we have chai!")



#how do you get data out of a loop

my_list = []

while len(my_list) < 5:
    my_var = input("give me a number")
    my_list.append(my_var)

print(my_list)