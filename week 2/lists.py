# In Python lists are ways of grouping together 
# similar things (usually)
the_count = [1, 2, 3, 4, 5]
stocks = ["FB", "APPL", "NFLX", "GOOG"]
random_things = [55, 1/2, "Puppies", stocks]

people = []

people.append("Mattan")
people.append("Daniel")
people.append("Sam")
people.remove("Daniel")

print(people)

cities = "New York, San Francisco, London".split(", ")

print(cities)
# allows you to get from a string into a list

print(", ".join(["milk", "eggs", "cheese"]))
# allows you to get from a list to a string

# Access elements of a list using square brackets
# Lists start at 0 (called 0 indexed)
first_city = cities[0]
second_city =  cities[1]
last_city = cities[-1]
first_two_cities = cities[0:2]
# -1 gives you the last item in the list
# [0:2] called slice notation--using for slicing things out of lists

print(first_two_cities)