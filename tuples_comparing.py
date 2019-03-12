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
