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

def slope_intercept(m, b, lower_x, upper_x):
    if lower_x > upper_x:
        return False
    
    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    m_i = input("please enter a value for slope (m) or exit to quit:")
    if m_i.lower() == "exit":
        break
    b_i = input("plese enter a value for the y-int (b) or exit to quit:")
    if b_i.lower() == "exit":
        break
    lower_x_i = input("please enter avalue for the lower x bound or exit to quit:")
    if lower_x_i.lower() == "exit":
        break
    upper_x_i = input("please enter a value for the upper x bound or exit to quit:")
    if upper_x_i.lower() == "exit":
        break

    m = num_converter(m_i)
    b = num_converter(b_i)
    lower_x = num_converter(lower_x_i)
    upper_x = num_converter(upper_x_i)

    result = slope_intercept(m, b, lower_x, upper_x)
    print(result)

print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def calc_sqrt(value):
    if value < 0:
        return None
    return value ** 0.5

def solve(a, b, c):
    discriminant = b ** 2 - 4*a*c
    sqrt_discriminant = calc_sqrt(discriminant)
    if sqrt_discriminant is None:
        return None, None
    
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2

while True:
    a_i = input("please enter a value for a or exit to quit:")
    if a_i.lower() == "exit":
        break
    b_i = input("please enter a value for b or exit to quit:")
    if b_i.lower() == "exit":
        break
    c_i = input("please enter a value for c or exit to quit:")
    if c_i.lower() == "exit":
        break

    a = num_converter(a_i)
    b = num_converter(b_i)
    c = num_converter(c_i)

solutions = solve(a, b, c)
if solutions == (None, None):
    print("no real solutions")
else:
    x1, x2 = solutions
    print(solutions)
