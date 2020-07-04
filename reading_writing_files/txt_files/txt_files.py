names = []

with open("names.txt") as txt_file: #txt_file is a variable can be called whatever. #with open puts everything in the block to extract then closes automatically
    for line in txt_file:
        print(line)
        line = line.strip() #removed the \n from the list (new line character)
        names.append(line)

print(names)

with open("names_output.txt", "w") as txt_file: #w means we are writing to this file. if you want to add into it you can use "a" for append
    for name in names:
        txt_file.write(name + "\n")

