#practice parsing strings
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

#string challenge
line = "X-DSPAM-Confidence:0.8475"
#challenge is to 1) extract everything after the colon, and 2)convert that value to a floating point number
line_2 = line.find(":")
line_3 = line[line_2+1:(len(line))] #holy shit this worked...I didn't think it would
answer = float(line_3)
print(answer)
print(type(answer))

#write a program to 1) prompt for file name, 2) read through the file and seek certain span of text
user_input = input("Please enter a file name:\n")
count = 0
total = 0
try:
    handle = open(user_input)
except:
    print("Sorry, that file name is incorrect or doesn't exist.")
    exit()
for i in handle:
    i = i.rstrip()  #strip out whitespace
    if i.find("X-DSPAM-Confidence") == -1:  #if the line does not include this text
        continue                            #ignore it and move to next line!
    count = count + 1       #as it proceeds, start counting lines it finds the above value
    found_1 = i.find(":")   #now seek the colon
    values = i[found_1+2 : (len(i))]    #seek difference between colon + space and end of text
    values = float(values)  #that span of text (the spam scores) are converted to floating point
    total = total + values  #add those values together into one large number
    answer = total / count  #divide that large number by the count established earlier
print("Average spam confidence:", answer)
