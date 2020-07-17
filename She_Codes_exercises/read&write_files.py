#Q1
# names = []

# with open("names.txt") as txt_file:
#     for line in txt_file:
#         line = line.strip()
#         names.append(line)

# print(names)

# for index, name in enumerate(names):
#     print(index, name)


#Question 2

# import csv

# colour_list = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour_list.append(line)

# #print(colour_list)

# for individual_colour in colour_list:
#     print(individual_colour[1], individual_colour[2], individual_colour[4])

# print("==================================")

# colour_list_2 = []

# with open("colours_213.csv") as csv_file2:
#     reader = csv.reader(csv_file2)
#     for line in reader:
#         colour_list_2.append(line)

# for individual_colour in colour_list_2:
#       print(individual_colour[1], individual_colour[2], individual_colour[4])


#Question 3


import csv
import pprint

colour_list = []
english_name_list = []
count = {}

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colour_list.append(line)

# for colour_name in colour_list:
#    print(colour_name[4])

for (colour_name) in (colour_list):
    english_name_list.append(colour_name[4])

for individual_colour in english_name_list:
    count.setdefault(individual_colour, 0)
    count[individual_colour] = count[individual_colour] + 1

individual_colour.get("red", 0) ###### UNFINISHED AND NOT WORKING YET!!!!!!!

#pprint.pprint(count)






