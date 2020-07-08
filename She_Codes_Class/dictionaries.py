groceries = { #curley brace for dictionary
    "Baby Spinach": 2.78, #Baby spinach is the key, number is the value
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "ORanges": 3.08
}

# print(groceries)

# print(groceries["Baby Spinach"])

groceries["Crakers"] = 2.50
print(groceries)

groceries["Avacado"] = 1.00 #to add another item into the dictionary.
print(groceries)

for item in groceries:
    print(item) # this corresponds to keys
    print(groceries[item]) #I can ask for the value of each of those keys by using square brace

print()

for item, price in groceries.items():
    print(item, price)


cohorts = {
    "perth": ["Anna", "Viv", "Nic", "Teagan"],
    "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
}
print(cohorts)

for cohort, peeps in cohorts.items():
    print(cohort)
    for peep in peeps:
        print(peep)
    print()


all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

for year, cohorts in all_cohorts.items():
    print(year)
    for city, cohort in cohorts.items():
        print(city, cohort)
        for peep in cohort:
            print(peep)

print(all_cohorts[2020]["perth"][0])




