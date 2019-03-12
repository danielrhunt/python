#finding largest and smallest values in a set

#find the largest value
largest = None
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i >= largest: #if the largest variable has no value, OR if whatever is in there is greater than or equal to what is encountered in the set...
        largest = i                     #replace it!
    print("Loop iteration:", i, largest)
print("The largest number in the set is: ", largest)

#find the smallest value
smallest = None
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i <= smallest:
        smallest = i
    print("Loop iteration:", i, smallest)
print("The smallest number in the set is: ", smallest)

#try combining them
largest_2 = None
smallest_2 = None
for i in [3, 41, 12, 9, 74, 15]:
    if largest_2 is None or i >= largest_2:
        largest_2 = i
    if smallest_2 is None or i <= smallest_2:
        smallest_2 = i
print("The REAL largest number in the set is: ", largest_2)
print("The REAL smallest number in the set is: ", smallest_2)

#the above code works, showing that you can use the same iteration variable several times in a sequence

#turning the above into functions:
def largest_value(values):  #sets up to inject set of values into the function
    largest = None
    for i in values:
        if largest is None or i >= largest:
            largest = i
    return largest #determines what output of the function should be...leave printed text out here and specify that in later output

#test the above:
test_set = [100, 1000, 2000, 37, 6000]
print("The largest number in the test set is:", largest_value(test_set))
print("The largest number in the test set is:", max(test_set)) #should be same as above
