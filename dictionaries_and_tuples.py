'''DICTIONARIES AND TUPLES'''

'''dictionaries have a method called ITEMS that returns a list of tuples,
where each tuple is a key-value pair'''

d = {"a" : 10, "b" : 1, "c" : 22}
print(d)
print(type(d))  #dictionary

t = list(d.items())     #turns into list!
print(t)
print(type(t))

'''because the variable t is a list (a list of tuples), and because tuples are comparable, we can now sort the list of tuples
converting a DICTIONARY to a list of tuples is a way for us to output the contents of a dictionary sorted by key'''

t.sort()
print(t)
print(type(t))

'''the output here is sorted in ascending alphabetical order by the key value'''

'''MULTIPLE ASSIGNMENTS WITH DICTIONARIES'''
'''you can combine ITEMS, TUPLE ASSIGNMENT, and FOR to produce a code pattern for traversing the keys and values of a dictionary in a single loop'''

for key, value in list(d.items()):
    print(value, key)

'''that loop has two iteration variables because ITEMS RETURNS A LIST of tuples and key
value is a tuple assignment that successively iterates through each of the key-value pairs in the dictionary
for each iteration through the loop, both key and value are advanced to the next key-value pair in the dictionary (still in hash order)'''

'''if we combine these two techniques, we can PRINT THE CONTENTS OF A DICTIONARY, sorted by the value stored in each key value pair
to accomplish this goal, we first make a list of tuples where each tuple is (value, key)
the ITEMS method would give us a list of (key, value) tuples, but this time we want to sort by value, not key
once we have constructed the list with the value-key tuples, it is a simple matter to sort the list in reverse order and print the new sorted list'''

d = {"a" : 10, "b" : 1, "c" : 22}
l = list()  #create empty list
for key, value in d.items():
    l.append( (value, key))
print(l)

l.sort(reverse = True)
print(l)

'''by carefully constructing the list of tuples to have the value as the first element of each tuple,
we can sort the list of tuples and get our dictionary contents sorted by value'''
