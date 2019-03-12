'''parsing lines'''

#here is reference line for what examples in mbox look like:
practice = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

#the goal here is to find the day of the week for all lines starting with "From:"
'''the SPLIT method is very effective for identifying lines with certain conditions
you can write a program to look for the lines (with given condition), SPLIT those lines,
and then print out the third word from the line'''

user_input = input("Please enter a file name:\n")
try:
    handle = open(user_input)
except:
    print("Sorry but that file doesn't seem to exist")
    exit()
for i in handle:
    i = i.rstrip()  #remove white space
    if not i.startswith("From "):
        continue
    #for everything else:
    words = i.split()   #create variable with lines left over (i.e. starting with From:)
    #and split them apart
    print(words[2]) #print third word in each split line

'''you can also use a "contracted" form of if statement, putting the "continue" up on the same line - I chose to not do that above'''
