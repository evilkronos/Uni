s = '1.23,2.4,3.123'
total = 0.0
for x in s.split(','):
    total = total + float(x)
print(total)
