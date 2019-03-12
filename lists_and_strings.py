#lists and strings
'''a string is a sequence of characters, and a list is a sequence of values
but a list of characters is not the same as a string
to convert from a string to a list of characters, you can use LIST'''

s = "spam"      #naturally creates a string
print(type(s))
t = list(s)     #leaves the string alone, but creates a new list with same values
print(t)
print(type(t))

'''however, when it pulls in that string, it treats each letter as it's own element'''
'''if you want to break a string into full words, you can use the SPLIT method'''
s = "pining for the fjords" #build a string
print(s)
print(type(s))
t = s.split()   #invoke a method so use dot notation
print(t)
print(type(t))

'''after you've used the split method to break a string into a list of words, you can use the index operator to look at specific words'''
print(t[2])

'''if needed, you can invoke split with a special argument called a DELIMITER
the delimiter specifies which characters to use as word boundaries
this can be helpful with oddly formatted data'''
example = "spam-spam-spam-gobbles-timmy"
print(example)
print(type(example))
fixed_example = example.split("-")
print(fixed_example)
print(type(fixed_example))

'''you can also write the delimiter as a variable, and inject that
this was how it was done in the text'''
example = "spam-spam-spam-gobbles-timmy"
print(example)
print(type(example))
delimiter = "-"
fixed_example = example.split(delimiter)
print(fixed_example)
print(type(fixed_example))

'''the inverse of split is JOIN, which is used to take a list of strings and concatenate the elements
join is a string method, so yuou invoke it on the delimiter and pass the list as a parameter
it's worth noting that this process TURNS A LIST INTO A STRING'''

example = ["oh", "no", "mr.", "bliss"]  #create the list
print(example)
print(type(example))
delimiter = " "     #basically saying "put the space in and bring together"
fixed_example = delimiter.join(example)     #start with the delimiter (i.e. what you want between the elements), and then add JOIN and pass in the variable
print(fixed_example)
print(type(fixed_example))

'''you could bring the whole thing together without spaces, by just passing in empty quotes'''
