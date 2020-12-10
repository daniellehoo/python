import random

dish = ["Spaghetti alla Carbonara",
"Meatloaf",
"Tuna Nicoise Salad",
"Lobster Mac and Cheese",
"Green Curry"]

guests = ["Sally",
"Sam",
"Bill Clinton",
"Barron Trump",
"Dan Harmon"]

random_meal = random.choice(dish)
random_guest = random.choice(guests)

print(f"Let's make {random_meal} and invite {random_guest} over for dinner tonight.")