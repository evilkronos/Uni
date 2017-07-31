def squareRootNewton(x):
    guess_y = float(x) / 2.0
    epsilon = 0.01
    global numGuess
    numGuess = 0
    while abs(guess_y*guess_y - float(x)) >= epsilon:
        numGuess += 1
        guess_y = guess_y - (((guess_y ** 2) - float(x)) / (2 * guess_y))
        print(guess_y,'-(',guess_y,'^2 -',x,')/(2*',guess_y,')')
    print('Square root of', float(x), 'is about', guess_y, 'This took ', numGuess, ' guesses.')

def squareRoot(y):

    epsilon = 0.01
    global numGuesses
    numGuesses = 0
    low = min(1.0, y)
    high = max(1.0, y)
    ans = (high + low)/2.0
    while abs(ans**2 - y) >= epsilon:
        print('low = ', low, 'high = ', high, 'ans = ', ans)
        numGuesses += 1
        if ans**2 < y:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to the Square root of', y)

def squarRootComparrison(x):
    squareRoot(x)
    squareRootNewton(x)
    if numGuess < numGuesses:
        print("The Newton-Raphson search took: ", numGuess,"This is faster than the Exhaustive search by", numGuesses - numGuess,"steps.")
    else:
        print("The Exhaustive search took: ", numGuesses, "This is faster than the Newton-Raphson search by",
              numGuess - numGuesses, "steps.")

x = float(input('Please enter a number to be squared by both algorithms:'))
squarRootComparrison(x)
