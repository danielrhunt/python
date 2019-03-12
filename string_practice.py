#practice with strings

fruit = "banana"
first_letter = fruit[0] #first always starts with zero
second_letter = fruit[1]
third_letter = fruit[2]
print(first_letter, second_letter, third_letter)

#to find the length of a string:
len(fruit)
print(len(fruit))

#to find the last letter in a string:
fruit_length = len(fruit)
last_letter = fruit[fruit_length-1] #tells it to go full length, and subtract one
print(last_letter)  #should be an "a"

#you could also do the above and find last letter in a much easier way:
fruit[-1]
print(fruit[-1])

#doing TRAVERSAL through a string
#you could use a WHILE loop, but it's extra complicated
#instead, opt for the FOR loop:
for i in fruit:
    print(i)

#a segment of a string is called a SLICE
#selecting a slice is similar to selecting a character:
practice = "Monty Python"
print(practice[0:5])
print(practice[6:12])

#if you omit the first index (before the colon), the slice starts at the beginning:
print(practice[:5])
#if you omit the second index (after the colon), the slice goes until the end:
print(practice[0:])
#so if you omit both, you get the entire string:
print(practice[:])
#if the first index is greater than or equal to the second, the result is an EMPTY STRING (represented by two quotation marks):
print(practice[3:3]) #actually just prints a blank line

#counting the NUMBER OF TIMES A LETTER APPEARS IN A STRING:
count = 0
for i in fruit:
    if i == "a":
        count = count + 1
print("The letter a appears in banana", count, "times.")

#let's try turning this into a program:
input_1 = input("Please enter a word or sentence:\n")   #prompts user to enter a word to sentence, with both working
input_2 = input("Please enter a letter for which you want to search in your previous entry:\n") #prompts user to enter a letter...anything longer doesn't seem to work
count = 0

for i in input_1:   #parse through what was entered by user
    if i == input_2:    #look for search character
        count = count + 1
print("The letter or phrase you entered was: ", input_1)
print("Your search term,", input_2, "appeared in that", count, "number of times.")

#TEXT REPLACEMENT
#remember that STRINGS ARE IMMUTABLE.  To make a change, you need to create a new variable into which you funnel the change(s):
start = "Hello, world!"
finish = "J" + start[1:]    #you can leave the second number blank after the colon
print(finish)               #this prints "Jello, world!"

finish_2 = "" + start[:-1]  #the nothing contained in the quotes effectively deletes the exclamation point
print(finish_2)

#comparison operators also work on strings
if fruit == "banana":
    print("Both words are banana")

#STRING METHODS
#Python can also be used to put words in alphabetical order.
#however, it's worth noting that Python does not handle uppercase and lowercase letters the same way as people
#to Python, ALL UPPERCASE LETTERS COME BEFORE ALL LOWERCASE LETTERS
#so to handle that, here's an example where I normalize a user input to all lowercase letters:

input_1 = input("Please enter a word:\n")
input_2 = input_1.lower()                   #convert to lower case
if input_2 < "banana":
    print("Your word,", input_1, "comes before banana.") #present back to user however they typed it in
elif input_2 > "banana":
    print("Your word,", input_1, "comes after banana.")
else:
    print("Your word is the same as the test word.")

#you can search for position of one string within another using the "find()" method...i.e. you're "invoking" find on a strings
#the find method can also find substrings (i.e. more than one character)
fruit = "banana"
found_fruit = fruit.find("ana")
print(found_fruit)

#and further, the find method can take a second argument, allowing a user to specify where to start searching
fruit = "banana"
found_fruit = fruit.find("ana", 3)
print(found_fruit)

#if you want to remove WHITE SPACE, you can use the STRIP method
line = " here we go again    "
print(line)
print(line.strip())

#you can check whether a line starts with a particular character
line = "Here I go again on my own"
#you'll get either a true or false value
line.startswith("h")
#and you'll notice it's case sensitive, so a good way to deal with this is to use the lower method
print(line.lower().startswith("h")) #NOTICE YOU'RE CHAINING THEM TOGETHER

#SO YOU CAN CHAIN METHODS TOGETHER...DO IT IN ORDER OF IMPORTANCE

#exercise from the book associated with counting characters in a string:
fruit = "banana"
count = 0
for i in fruit:
    if i == "a":
        count = count + 1
print("The letter 'a' appears in banana", count, "times.")

#you can use the FIND and SLICE methods to take only pieces of strings
practice = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"   #create practice string
found_1 = practice.find("@")    #finds position about half way through
found_2 = practice.find(" ", found_1)    #telling it to start the find at position found in first find
#the above will tell it to start after the @ sign, and extract the email domain and stop at the first blank space it sees
email_domain = practice[found_1+1:found_2]
print(email_domain)

#the FORMAT OPERATOR
#the format operator is % when looking at a string (and not a modulo)
#it allows you to replace parts of the string(s), with data store in a variable
#the result after being formatted is a string, even if you used an integer value...
#however, you can use %d to indicate the value stored within a string is a decimal value
#here is the difference:
camels = 42
print("%d" % camels)    #prints the string "42"

#you can further embed the value into a sentence:
print("I have spotted %d camels in the wild" % camels)  #this works and prints the statement

#a TUPLE is a sequence of comma separated values inside a pair of brackets
#if there is more than one format sequence for a string, the second argument must also be a tuple (to account for what's going into the string)
#the types of elements must match the format sequences
#the number of elements must match the number of format sequences in the string
print("In %d, I have spotted %g %s in the wild" % (3, 42, "camels"))    #this works but see below
#NOT SURE WHY THE VARIOUS LATTERS ARE BEING USED AFTER THE FORMAT OPERATOR
