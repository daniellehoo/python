# Intro to Programming Using Python - Assignment #1
# Completed by: Mattan Griffel

# 1. Print out the following text: 
# You've reached [your name]. 
# I'm not available right now, so leave a message and I'll call you back.
print("You've reached Mattan Griffel.")
print("I'm not available right now so leave a message and I'll call you back.")

# 2. Create five variables for your first name, last name, shoe size, height, and age. 
# And then print them out on one line.
first_name = "Mattan"
last_name = "Griffel"
shoe_size = 10.5
height = 70
age = 29
print(first_name, last_name, shoe_size, height, age)

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
subtotal = 10.58
tip = 0.22
total = subtotal * (1 + tip)
print(total)

# 4. Convert 158.8 into an integer. 
# Convert 75 into a float. 
# Convert "244.9" into a float and then an integer.
int(158.8)
float(75)
int(float("244.9"))

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# —in the woods
#               which
#                   stutter
#                           and
# 
#                               sing
print("-in the woods\n\t\twhich\n\t\t\tstutter\n\t\t\t\tand\n\n\t\t\t\t\tsing")

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: 
# Mattan, your total is $12.91 
# (remember to round the total to the nearest cent)
print(f"{first_name}, your total is ${total:.2f}")

# 7. Use input() to ask a user for the city they live in, and then print it back to them.
city = input("What city do you live in? ")
print("Ahhh beautiful", city)

# 8. Build a future value calculator by using input() to get values from the user. 
# (Make sure you convert them into integers or floats before doing any math on them.) 
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods
present_value = float(input("What is the present value? "))
rate_of_return = float(input("What is the rate of return? "))
number_of_periods = int(input("What is the number of periods? "))
future_value = present_value * (1 + rate_of_return) ** number_of_periods
print("The future value is:", future_value)
