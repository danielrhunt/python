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
