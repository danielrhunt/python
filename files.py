#learning files (larger document)
handle = open("mbox.txt")
print(doc)
#if you're successful, the operating system returns a file HANDLE which allows you to read data

#count the number of lines in a file
handle = open("mbox.txt")
count = 0
for i in handle:
    count = count + 1
print("The number of lines in the file is:", count)

#when data is read in this manner, Python is careful to take note of the newline character and split acccordingly
#if you're ready to READ the file, you can put it all into a single string using the READ method on the file handle:
handle = open("mbox-short.txt")
doc = handle.read()
print(doc[:20]) #use string SLICING to read only first twenty characters

#remember that everything from the above read() is now one big string in the "doc" variable
#only use this form of method (read) if you're confident the file can be successfully loaded into memory on your device
#if the file is too large, use a FOR or WHILE loop to read the file in chunks

#when searching through data in a file, it's very common to ignore most lines and only process lines meeting certain conditions
#to accomplish this goal, combine reading a file with various string methods
#for example, to PRINT LINES ONLY MEETING CERTAIN CONDITIONS, you could do the following:
handle = open("mbox-short.txt")
count = 0       #not sure what this is doing in the code...maybe used later? NOTE: looks like a mistake in the book
for i in handle:
    if i.startswith("From:"):   #specifies only to activate if iteration variable finds \n with From: condition
        print(i)

#that works great, and prints all the addresses that sent emails; but it also leaves double spaces, because each line ends with a newline
#to STRIP OUT NEWLINES, you can use the RSTRIP method to remove whitespace from the right side of the string
handle = open("mbox-short.txt")
for i in handle:
    i = i.rstrip()      #strip out all white space
    if i.startswith("From:"):
        print(i)
#as the programming gets more complicated, it's a good idea to explicitly skip non-interesting lines using the CONTINUE statement
handle = open("mbox-short.txt")
for i in handle:
    i = i.strip()
    if not i.startswith("From:"):   #if the line DOES NOT start with From:
        continue                    #skip it!
    print(i)                        #print what remains

#you can also allow the user to choose their own files to open!
#and count the number of emails in that file!
user_input = input("Please choose your file name:\n")
handle = open(user_input)
#you can further add some code to check if it's working, like doing a count of all the lines in the file
count = 0
for i in handle:
    if i.startswith("From:"):   #search for each new email sent
        count = count + 1
print("There are", count, "emails contained in this file.")

#however, this doesn't take into account the likelihood that a user could enter an incorrect file, or a file that doesn't exist
#for these situations, it's always good to use a TRY/EXCEPT when prompting the user for input
user_input = input("Please type the name of the file you wish to open:\n")
try:
    handle = open(user_input)
except:
    print("Sorry, this file doesn't seem to exist.")
    exit()      #this terminates the program
count = 0
for i in handle:
    if i.startswith("From:"):
        count = count + 1
print("There are", count, "emails contained in this file.")

#practice using FIND in strings
handle = open("mbox-short.txt")
for i in handle:
    i = i.rstrip()  #strip whitespace from right side of string
    if i.find("@uct.ac.za") == -1:
        continue    #basically saying if the line DOES NOT start with that domain, skip it!
    print(i)        #print what remains in the string line


#to write a file, you need to open it with "w" as a second parameter
#the file object keeps track of where it is, so if you call WRITE again, it adds new data to the end
#when you are done writing, you need to close the file to ensure data is physically written to the disk
example_1 = open("output.txt", "w")
print(example_1)

#the above created a new file in my python folder on the desktop
#it was an empty file
#let's see if we can add some text to it

line_1 = "Tommy used to work on the docks\n"
line_2 = "Union's been on strike, he's down on his luck, it's tough\n"
line_3 = "so tough"

#that created several variables, but didn't write them to the file on the desktop
#to accomplish that goal, let's try this:
example_1.write(line_1)

#it worked!
#let's add some more lines...
#example_1.write(line_1, line_2, line_3)  <--- does not work!!

#if this works, we should see all the text go in there but not see a delineation between lines 2 and 3...
#it didn't work - WRITE ONLY TAKES ONE ARGUMENT

example_1.write(line_1)
example_1.write(line_2)
example_1.write(line_3)

#this time it worked, but need to fix that newline (fixed above)
#however, because it has line_1 written twice, it appears twice in the file

example_1.close()
