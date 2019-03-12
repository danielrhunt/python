'''THE MOST COMMON WORDS'''

'''this example looks at text and prints the ten most common words'''

import string

user_input = input("Please enter a file name:\n")
try:
    handle = open(user_input)
except:
    print("That file does not exist in this directory.")
    exit()

counts = dict() #create empty dictionary
for line in handle:
    line = line.translate(string.punctuation)   #removes punctuation to make consistent
    line = line.lower()     #converts to all lowercase
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#sort the dictionary by value
user_list = list()  #create empty list
for key, value in list(counts.items()):
    user_list.append((value, key))

user_list.sort(reverse = True)

for key, value in user_list[:10]:
    print(key, value)
