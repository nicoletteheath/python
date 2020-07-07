spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is " + str(spam)) 
#in this example this print function doesn't occur for 3 because the statement above and the continue means
# it goes back to the beginning without doing the print function. 
