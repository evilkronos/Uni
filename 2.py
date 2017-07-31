

largestOddNumber = None
for _ in range(10):
    number = int(input('Enter an integer:'))
    if (number % 2 != 0) and (largestOddNumber is None or number > largestOddNumber):
        largestOddNumber = number

if largestOddNumber is not None:
    print("The largest odd number you entered is: " + str(largestOddNumber))
else:
    print("No odd number was entered")

