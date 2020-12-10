# Variables are just nicknames
# they're plain, lowercase words
# convention: lowercase words and underscores

name = "Danielle Hoo"
orphan_fee = 200
teddy_bear_fee = 121.80
total = orphan_fee + teddy_bear_fee

print(name, "the total will be", total)

# you can't use variables that haven't been created yet

print(f"{name} the total will be ${total:.2f}")