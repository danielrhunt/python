#learning to open files
#remember that the newline character "\n" counts as a single character

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
