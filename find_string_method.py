#more practice using the find method on strings

handle = open("mbox-short.txt")
for i in handle:
    i = i.rstrip()  #strip whitespace from right side of string
    if i.find("@uct.ac.za") == -1:
        continue    #basically saying if the line DOES NOT include that domain, skip it!
    print(i)        #print what remains in the string line
