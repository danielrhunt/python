#practicing with functions

#create a function
def print_lyrics():    #this is the HEADER, and the FUNCTION DEFINITION is "print lyrics"
    print("Livin' on a prayer")     #this begins the BODY of the function, which is everything that follows
    print("without a care!")

print(print_lyrics)     #this only prints some random text, and doesn't execute the function
print_lyrics()   #you don't need to add "print" to execute...but remember to add parentheses, as it will execute the function!

def print_lyrics_var(i):    #here we've added an iteration variable, which is now required to run the function
    print("Livin' on a prayer,", i)
    print(i, ", really don't care!")

print_lyrics_var("Dan")  #Putting "Dan" in as iteration variable plugs it in for "i" throughout
#remember you don't need to put this in a "print" to make it print in a terminal!!!

#the first character of a function cannot be a number!
#avoid using a variable name as beginning of a function
#the empty parentheses after the name of a function (first example) indicate it doesn't take any "arguments"
#single and double quotes do the same thing, but I like using double quotes better to protect against apostrophes
#REMEMBER that a function definition has to be executed before it's called in a code

#You can use built in modules, if desired...just make sure you import them
import math
def print_equation(k):
    k = int(k)                  #make sure to convert the string to an integer
    print((math.pi * k) - k)

m = input("Please enter a numeric digit\n")
print_equation(m)

'''when you're creating a function, you can make inputs optional by setting them to "none"'''
def add_numbers(x, y, z=None):
    if z == None:               #if you make it optional, must account with IF statement
        return x + y
    else:
        return x + y + z

def add_numbers(x, y, z=None):
    if (z == None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))
