#practicing writing files in Python
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
