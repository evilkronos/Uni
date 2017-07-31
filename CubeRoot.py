#x = int(input('Enter an integer: '))
#ans = 0
#while ans **3 < abs(x):
    #print('Value of a decrementing function abs(x) - ans**3 is', abs(x) - ans**3) Used to determine the cuase of the indefinate loop, why the distance between ans**3 and abs(x) is not reducing
#    ans = ans + 1
#if ans **3 != abs(x):
#    print(x, 'is not a perfect cube')
#else:
#    if x < 0:
#        ans = -ans
#    print('Cube root of', x, 'is', ans)


import math
integer = int(input("Please enter an integer: "))
for pwr in range(1,6):
    root = (integer ** (1.0/pwr))
    if math.ceil(root) == root:
        print(root, pwr)
    else:
        print("No matching root for the power: ", pwr)


 #   a = (integer ** (1.0/power))
 #   if math.ceil(a) == a:
   #     print(a, power)
