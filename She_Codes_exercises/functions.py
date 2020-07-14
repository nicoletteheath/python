# Question 1
#(F - 32)*5/9 = C

# fahrenheit_temperature = input("what is the temperature in fahrenheit? ")
# celsius_temperature = (float(fahrenheit_temperature) - 32.0) * 5.0 / 9.0
# print(f"{celsius_temperature:.2f}")

def convert_fahrenheit(temp_in_fahrenheit):
    celsius_temperature = (float(temp_in_fahrenheit) - 32.0) * 5.0 / 9.0
    return celsius_temperature

print(convert_fahrenheit(113))



 #Question 2
 #mean is the sum divided by the count (average of the numbers)


def calculate_mean(total_sum, num_items):
    mean = total_sum / num_items
    return mean

print(calculate_mean(50, 10))



# output_numbered_list = False
# number_list = []
# while output_numbered_list == False:
# number = input("Enter a number")
# if number == "":
#     output_numbered_list = True
# else:
#     number_list.append(int(number))
# return(number_list)

# total_sum = sum(number_list)
# num_items = len(number_list)






