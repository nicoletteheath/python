def hello(): #uses def statement to define a new function called hello
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")

hello() #only runs when the function is called. at that point moves inside the function. 
hello()
hello()

def hello(name): #name is called a paramater
    print("Hello " + name)
  
hello("Alice") #Alice is an argument
hello("Bob")

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

