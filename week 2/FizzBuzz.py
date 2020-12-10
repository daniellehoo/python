# FizzBuzz.py
# Print numbers from 1-100
# For multiples of 3 print "Fizz"
# For multiples of 5 print "Buzz"
# For multiples of both 3 and 3, print "FizzBuzz"

fizz_buzz = []
for number in range(1, 101):
    if ((number % 3 == 0) and (number % 5 == 0)):
        fizz_buzz.append("fizzBuzz")
    elif ((number % 3) == 0):
        fizz_buzz.append("fizz")
    elif ((number % 5) == 0):
        fizz_buzz.append("buzz")
    else: fizz_buzz.append(number)

print(fizz_buzz)

#FizzBuzz Mattan's solution
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: print(number)
    # print (number)