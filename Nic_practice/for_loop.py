print("My name is")
for i in range(5):
    print("Jimmy Five Times " + str(i))

total = 0
for num in range (101):
    total = total + num
print(total)


# using a while statement rather than a for loop for the first exercise
print("My name is")
i = 0
while i < 5:
    print("Jimmy Five Times " + str(i))
    i = i + 1

# using the range to change from 0 - 4 to 12 - 15
print("My name is")
for i in range(12, 16):
    print("Jimmy Five Times " + str(i))

# within range bracket have start, end, how much it changes by each time
print("My name is")
for i in range(0, 10, 2):
    print("Jimmy Five Times " + str(i))


# change last number to negative number to count down.
print("My name is")
for i in range(5, -1, -1):
    print("Jimmy Five Times " + str(i))