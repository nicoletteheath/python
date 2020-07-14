#Q1
names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)

print(names)

for index, name in enumerate(names):
    print(index, name)




# for index, name in enumerate(names): #will result in number next to item
#     print(index, tea)