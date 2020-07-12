import pprint

message = "It was a bright cold day in April, and the clocks were stiking thirteen."
count = {} #"r":12

for character in message.upper(): #upper() returns an uppercase form of the string
    count.setdefault(character, 0) #sets the counter to 0
    count[character] = count[character] + 1

pprint.pprint(count)

#Apriltext = pprint.pformat(count)
#print(Apriltext)

# pformat function returns the string (instead of being printed to the screen)
