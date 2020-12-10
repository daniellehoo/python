# Intro to Programming Using Python - Assignment #1
# Completed by: Danielle Hoo

# 1. Print out the following text: 
# You've reached [your name]. 
# I'm not available right now, so leave a message and I'll call you back.


print(f"You've reached Danielle. \
I'm not available right now, so leave a message and I'll call you back.")

# 2. Create five variables for your first name, last name, shoe size, height, and age. 
# And then print them out on one line.

first = "Danielle"
last = "Hoo"
shoe_size = 9
height = 65
age = 32

print(f"First: {first} Last: {last} Shoe Size: {shoe_size} Height: {height} Age: {age}")

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.

subtotal = 10.58
tip = 0.22
total = subtotal + (subtotal * tip)

print(f"Total: ${total:.2f}")

# 4. Convert 158.8 into an integer. 
# Convert 75 into a float. 
# Convert "244.9" into a float and then an integer.

integer_var = int(158.8)
float_var = float(75)
int_and_float = int(float(244.9))

print(integer_var, float_var, int_and_float)

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
# 
#                               sing

print("-in the woods \n \t \t which \n \t \t \t stutter \n \t \t \t \t and \n \t \t \t \t \t sing")

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: 
# Mattan, your total is $12.91 
# (remember to round the total to the nearest cent)

print(f"{first}, your total is ${total:.2f}")

# 7. Use input() to ask a user for the city they live in, and then print it back to them.

city = input("What city do you live in? ")

print(f"You live in: {city}")

# 8. Build a future value calculator by using input() to get values from the user. 
# (Make sure you convert them into integers or floats before doing any math on them.) 
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

present_value = float(input("What is the present value? "))
rate_of_return = float(input("What is the rate of return? "))
number_of_periods = int(input("What is the number of periods?"))
future_value = present_value*(1 + rate_of_return)**number_of_periods

print(f"The future value is: {future_value}")