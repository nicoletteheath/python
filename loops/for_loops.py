tea_collection = [
    "Earl Grey",
    "Melbourne Breakfast",
    "Chai",
    "Peppermint",
    "Lemon and Ginger",
    "Strawberry Cream",
    "Chamomile",
    "Green",
    "Dandelion"
]

# for tea in tea_collection: #for each of the items in tea_collection, tea is the variable. so you could replace tea with any word. 
#     #print(tea)
#     # print(type(tea)) #everythinig indented is going to be inside the for loop
#     print(f"I have {tea} flavoured tea.")

# print("ended loop")

# for index in range(0, 10): #start to 0 go up to 10 but last one isn't counted #index is name of variable - again can be whatever. if using numbers common to use index.
#     print(index)

# for index in range(0, 50, 5): # same as above 0-50 but last one not counted but in steps of 5. start, stop, multiples
#     print(index)

# for index, tea in enumerate(tea_collection): #will result in number next to item
#     print(index, tea)

tea_collection = [
    ["Black", "Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Flavoured", "Peppermint", "Lemon and Ginger", "Strawberry Cream"],
    ["Health", "Chamomile", "Green", "Dandelion"]
]

for tea_category in tea_collection:
    print(f"{tea_category[0]} Teas:")
    for tea in tea_category[1:]:
        print(f"    {tea}")

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}") #2f is for the 2 decimal points?


