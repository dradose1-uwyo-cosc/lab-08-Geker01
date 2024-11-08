# Garrett Eker
# UWYO COSC 1010
# 11/7/24
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def num_converter(num):
    isneg = False
    if "-" in num:
        isneg = True
        num = num.replace("-", "")
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isneg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isneg:
            return -1 * int(num)
        else:
            return int(num)

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    slope = input("please enter a value for the slope m or exit to quit")
    if slope.lower()== "exit":
        break
    y_int = input("please enter a value for the y-intercept b or exit to quit")
    if y_int.lower() == "exit":
        break
    lower_x = input("please enter a value for the lower x bound or exit to quit")
    if lower_x.lower() == "exit":
        break
    upper_x = ("please enter a value for the upper x bound or exit to quit")
    if upper_x.lower() == "exit":
        break

def slope_intercept(m, b, lower_x, upper_x):
    if lower_x > upper_x:
        return False
    y_values = [m * x + b for x in range(lower_x, upper_x)]
    return y_values

user_input = input("please enter four parameters for slope, x, an upper bound, and a lower bound or exit to stop:")
num_converter(user_input)



print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
