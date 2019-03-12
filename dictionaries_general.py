'''experimenting with dictionaries'''
'''a dictionary is like a list, but more generalized
in a list, the index positions have to be integers
in a dictionary, the indices can be almost any type
think about a dictionary as a mapping between a set of indices (which are called KEYS) and a set of values
each key maps to a value - this is called a KEY-VALUE PAIR, and sometimes called an ITEM
the function DICT creates a new dictionary with no items
'''

english_to_spanish = dict() #create new dictionary
print(english_to_spanish)
#it prints {}

'''the curly brackets represent an empty dictionary
to add items to the dictionary, you use square brackets'''

english_to_spanish["one"] = "uno"
print(english_to_spanish)

'''this output format - it prints {'one': 'uno'} - is also an input format
for example, you can create a new dictionary with three items
but you need to remember that the output order of a dictionary is totally unpredictable...
that's because elements of a dictionary don't use integer indices
instead, you look up items in a dictionary by using "keys", which help find the corresponding value'''

english_to_spanish = {"one" : "uno", "two" : "dos", "three" : "tres"}
print(english_to_spanish)
print(english_to_spanish)
print(english_to_spanish["two"])    #this invokes and prints only the matching item

'''if the item you request isn't in your dictionary, you'll get a "keyerror"
so for example, if you tried searching for "four" in the dictionary above, it wouldn't work'''

'''you can invoke certain functions like length on a dictionary, to figure out how many entries it has'''
print(len(english_to_spanish))

'''you can also invoke the IN operator on dictionaries, to determine if a certain KEY is in there
it will ONLY work on keys - it will not find matching elements!!!'''
print("one" in english_to_spanish)  #will return TRUE
print("uno" in english_to_spanish)  #will return FALSE, even though uno is in there as a matching element
print("four" in english_to_spanish) #will return FALSE, because it's not in there in any respect

'''instead, to see if something appears as a VALUE (element) in a dictionary, you need to invoke a special method'''
print("uno" in english_to_spanish.values()) #now will print TRUE

'''using a dictionary as a set of COUNTERS'''
'''you can use a dictionary as a counter to perform calculations, such as how many times a given letter appears in a string
the advantage of using the dictionary approach for this challenge (as opposed to other options) is that you don't need to know every possibility going in
to accomplish this goal, you would create a dictionary with CHARACTERS AS KEYS and COUNTERS as the corresponding value(s)
the first time you see a character, you add the item to your dictionary
after that, you increment the value of an existing item'''

#here is an example for how to accomplish this task
#this is basically computing a histogram
word = "brontosaurus"
print(type(word))
d = dict()
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)

'''dictionaries have a method called GET that takes a key and a default value
if the key appears in the dictionary, GET will return the corresponding value...otherwise it returns the default value'''
counts = {"chuck" : 1, "annine" : 42, "jan" : 100}
print(counts.get("jan", 0))     #zero is default value
print(counts.get("tim", 0))

'''because the GET method automatically handles the case where a key is not in a dictionary, it can be used to more easily count and thus eliminate the IF statement:'''

word = "brontosaurus"
print(type(word))
d = dict()
for i in word:
    d[i] = d.get(i, 0) + 1  #the "get" does the exact same thing as the "if/if not in" listed above
print(d)

'''a common use of a dictionary is to COUNT THE OCCURRENCE OF WORDS in a file with written text
the way you do this is to read through the lines in the file, break each line into a list of words, and then loop through each of the words in the line and count each word using a dictionary
this will be done with two FOR loops
the outer loop is reading the lines of the file
and the innter loop is iterating through each of the words on that particular line
this is called NESTED LOOPS (one outer, the other inner)
NOTE that the inner loop executes all of its iterations each time the outer loop makes a single iteration...
you can think of the inner loop as iterating "more quickly"
the combination of the two nested loops ensures that we will count every word on every line'''

'''dictionaries looping through files'''
'''to count the words and their distribution in a file...
this code will generate an unsorted output of all the words and their counts:'''

user_input = input("Please enter a file name:\n")
try:
    handle = open(user_input)
except:
    print("Sorry, that file does not appear to exist.")
    exit()

counts = dict()     #create empty dictionary to store values
for i in handle:    #loop through file
    words = i.split()   #looks for spaces and treats each word as a token separated by a space
    for k in words:
        if k not in counts:
            counts[k] = 1
        else:
            counts[k] += 1
print(counts)

'''if you use a dictionary as the sequence in a FOR statement, it traverses the keys of the dictionary
this loop will print each key and the corresponding value (in no particular order):'''

counts = {"chuck" : 1, "annie" : 42, "jan" : 100}
for key in counts:
    print(key, counts[key])

'''if you wanted to set a higher threshold for what to print, you could do something like this:'''

counts = {"chuck" : 1, "annie" : 42, "jan" : 100}
for key in counts:
    if counts[key] > 10:        #only return keys with values greater than ten
        print(key, counts[key])

'''now important to NOTE, we must use the index operator to retrieve the corresponding value for each key
this is because the FOR loop iterates through the keys of the dictionary
the square brackets denote that index value for the key'''

'''if you want to print the keys in ALPHABETICAL ORDER, you first make a list of the keys in the dictionary using the KEYS METHOD
the KEYS METHOD is found in the DICTIONARY OBJECTS
you then sort that list and loop through the sorted list, looking for each key and printing out key-value pairs in sorted order
demonstrated here:'''

counts = {"chuck" : 1, "annie" : 42, "jan" : 100}
key_list = list(counts.keys())  #create variable housing a list of keys, invoked using keys method
print(key_list) #prints a list of keys
print(type(key_list))   #confirmed that this is a list that was created
key_list.sort()         #sorts the list alphabetically
print(key_list)
print(type(key_list))
for key in key_list:        #now loop through sorted list
    print(key, counts[key]) #print each entry (now in alphabetical order), followed by it's index value

'''now for ADVANCED TEXT PARSING'''
'''the SPLIT function is inadequate to do advanced text parsing (on its own) because it doesn't take capitalization or punctuation into account
it would therefore treat words like "soft" and "soft!" and "Soft" as different words, and thus assign different counts
we can solve this problem by using string methods LOWER, PUNCTUATION, and TRANSLATE
we will also use the DELETECHARS parameter to delete all of the punctuation'''

import string
print(string.punctuation)   #show list of what python considers punctuation

import string

user_input = input("Please enter a file name:\n")
try:
    handle = open(user_input)
except:
    print("That file does not appear to exist.")
    exit()

counts = dict()     #create empty dictionary
for line in handle:
    line = line.rstrip()    #remove white space
    #translate to remove all punctuation
    line = line.translate(line.maketrans("", "", string.punctuation))
    #use lower to force the line to lowercase
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
