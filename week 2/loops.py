# Use for to loop over a list
numbers = [1, 2, 3]
for number in numbers:
    print(number)

numbers = [1, 2, 3]
number = numbers[0]
print(number)
number = numbers[1]
print(number)
number = numbers[2]
print(number)

stocks = ["fb", "aapl", "ntfx", "goog"]
for stock in stocks:
    print(stock.upper())

# looping challenge
# numbers = range(1, 100)
for number in range(1, 101):
    print(number ** 2) 

# You can do more than just print in a for loop
squares = []
for number in range(1, 101):
    squares.append(number**2)
print(squares)

# List comprehension
print([stock.upper() for stock in stocks])