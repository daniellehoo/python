numbers = [0]
for number in numbers:
    if number < 100:
        numbers.append(numbers[-1] + 1)
        for number in numbers:
            print(number ** 2)
    # else: print(numbers)