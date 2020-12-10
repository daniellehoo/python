
name = input("What is your name? ")
check = int(input("What is the total bill amount?" ))
fifteen_percent = check * .15
twenty_percent = check * .20
twenty_five_percent = check * .25

print(f"Hello, {name} here are the suggested tip amounts: \
    15%: ${fifteen_percent:.2f} \
    20%: ${twenty_percent:.2f} \
    25%: ${twenty_five_percent:.2f}")