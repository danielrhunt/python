#count the number of items in a list

#this example will add up the number of numbers in the set
#it shows the number of values encountered so far in the set
count = 0
for i in [3, 41, 12, 9, 74, 15]:
    count = count + 1 #this adds up the number of numbers in set, but doesn't sum them
print("The number of items in the set is:", count)

#this example will compute the total value of the numbers in the set
total = 0
for i in [3, 41, 12, 9, 74, 15]:
    total = total + i
print("The total sum of all values in the set is: ", total)

#so now let's find the average
count = 0
total = 0
for i in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    total = total + i
    set_average = total / count
print("The average value in the set is: ", set_average)

#it's worth remembering that "None" is a special constant value which can be used to show a variable is empty

#count the number of lines in a file
handle = open("mbox.txt")
count = 0
for i in handle:
    count = count + 1
print("The number of lines in the file is:", count)
