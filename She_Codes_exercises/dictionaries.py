
#exercise 2
import pprint

names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagan",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sohpie", "Teagen", "Viv"
]

count = {}

for individual_name in names:
    count.setdefault(individual_name, 0)
    count[individual_name] = count[individual_name] + 1
pprint.pprint(count)
