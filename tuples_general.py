'''learning about TUPLES'''
'''a tuple is a sequence of values, a lot like a list
the values stored in a tuple can be any type, and they are indexed by integers
the important difference between lists and tuples is that TUPLES ARE IMMUTABLE
tuples are also comparable and hashable
that's good because it means we can sort lists of them
we can also use tuples as key values in Python dictionaries'''

'''TUPLES ARE COMPARABLE!!!'''

'''a tuple is a comma-separated list of values
and common practice is to enclose tuples in parentheses
this helps to quickly identify tuples when viewing Python code'''

example = ("a", "b", "c", "d", "e")
print(type(example))

'''to create a tuple with a single element, you must include the final comma'''
yes_tuple = ("a",)      #will show as a tuple
print(type(yes_tuple))
no_tuple = ("a")        #will show as a string
print(type(no_tuple))

'''you can also construct a tuple using the built in TUPLE function
with no argument given, it creates an empty tuple
if you pass in a sequence (string, list, or tuple) into the tuple function, the output is a tuple with the elements of the sequence'''
example = tuple("lupins")
print(example)
print(type(example))

'''you can use list operators on tuples, and slice operators'''
print(example[1])
print(example[0:3])

'''you cannot pass more than one argument into the tuple function!!!!'''
example = tuple("lupins", "gobbles")    #won't work
print(example)      #won't work
print(type(example))    #won't work

'''you also cannot attempt to modify one of the elements of the tuple
however, you CAN replace one tuple with another:'''

example = ("a", "b", "c", "d", "e")
print(example)
example = ("A",) + example[1:]  #remember, if you used 0 spot it would put the A before the a
print(example)

'''COMPARING TUPLES'''
'''comparison operators work on tuples, just like other sequences
Python starts by comparing the first element in each sequence
if they are equal, it goes on to the next element, and then on again, and again, until it finds elements that differ
subsequent elements are not considered (even if they are really big)'''

'''the SORT FUNCTION works the same way: it sorts primarily by first element, but in case of a tie, it moves onto the next element until the tie is broken
this feature lends itself to a pattern called DSU: DECORATE, SORT, and UNDECORATE'''

example = "but soft what light in yonder window breaks"
print(example)
print(type(example))

words = example.split() #this doesn't appear to do anything on its own
tt = list() #create empty list
for word in words:
    #build list of tuples, where each tuple is preceded by it's length
    tt.append((len(word), word))    #add length of word, and then the word
print(tt)       #prints list in original order, preceded by count
print(type(tt))

#the sort compares the first element (length) first, and only considers the second element to break ties
#reverse = True tells sort method to go in decreasing order
tt.sort(reverse = True)     #reverse number sort (i.e. starts at highest)
print(tt)       #prints list in number sorted order (highest to lowest)
print(type(tt))

#this loop traverses the list of tuples, and builds a list of words in descending order of length
#the four character words are sorted in reverse alphabetical order
res = list()    #create another empty list
for length, word in tt:  #use two mnemonically named iteration variables
    res.append(word)    #append the words to res list

print(res)  #should just print the words
print(type(res))

'''TUPLE ASSIGNMENTS'''

'''one of the unique features of Python language is the ability to have a tuple on the left side of an assignment statement
this allows you to assign more than one variable at a time, when the left side is a sequence'''

#here is a two element list (which is a SEQUENCE)
m = ["have", "fun"]
print(m)
print(type(m))

#now we can assign the first and second elements of the sequence to the variables x and y in a single statement
x, y = m    #this turns them from list into string
print(x)
print(type(x))  #string!
print(y)
print(type(y))  #string!

'''you can also SWAP VALUES using the tuple assignment'''
a, b = b, a

'''both sides of that statement are tuples
the number of variables on the left, and the number on the right, must be the same!!!
more generally, the RIGHT SIDE can be any kind of sequence (string, list, tuple)
for example, to SPLIT AN EMAIL ADDRESS into a user name and domain, you could write:'''

email_address = "monty@python.org"
print(email_address)
user_name, domain = email_address.split("@")
print(user_name)
print(domain)
print(type(domain))

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
