#to calculate max and min using loops
#to calculate the MAX value
largest = None
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest: #first loop gives value of None, then grows from there
        largest = i
print("The largest number in the set is:", largest)

#to calculate the MIN value
smallest = None
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
print("The smallest number in the set is:", smallest)
