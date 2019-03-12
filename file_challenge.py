#file challenge
#exercise 7.1

#prompt user for the file

user_input = input("Please enter the file you wish to open:\n")
try:
    handle = open(user_input)
except:
    print("Sorry, but that file doesn't seem to exist.")
    exit()

for line in handle:
    print(line.upper().rstrip())

#it all works as expected
#wrote this all from memory
