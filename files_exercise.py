#files exercise

#exercise 1
#objective is to read a file and print contents in all uppercase
#I literally wrote this from memory on my first try and it worked
handle = open("mbox-short.txt")
file_1 = handle.read().upper()
print(file_1)

#exercise 2
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
