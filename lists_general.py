#practice with lists

'''#like a string, a LIST is a sequence of values
#to differentiate, know that a string can ONLY contain characters
#however, a LIST can be any type
#the values in a list are called ELEMENTS (or sometimes called "items")
#the simplest way to create a list is to enclose the values inside square brackets'''

practice = [11, "Timmy", 13]
print(practice)
print(type(practice))
print(len(practice))    #should be length of three

'''^ that is indeed a list, and prints as such
as noticed, you can have lists with mixed value types
lists can also contain another list(s) within, which is called a NESTED list
nested lists only count as a single element within the parent list'''

practice_2 = [11, 25, "Gobbles", [1, 2, 3], 35]
print(practice_2)
print(type(practice_2))
print(len(practice_2))  #should be length of five

#a list that contains no elements is called an EMPTY LIST
#you can print +1 list(s) using print:
print(practice, practice_2)

#the syntax for accessing the elements of a list are the same as accessing characters in a string:
print(practice_2[0, 2])   #that should print values 11 and "Gobbles"

#unlike strings, lists are MUTABLE - this means they can be changed!
#this is the case because you can change order of items in a list, or change their values
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[3] = 1  #that will change value of 4 to now be 1
print(numbers)

#you can think of a list as a relationship between indices and elements: this is called MAPPING - each index "maps to" one of the elements
#list indices work the same way as string indices: if an index has a negative value, it counts backward from the end of the list

#the "in" operator also works well on lists, in that youc an pose questions (sort of) with it:
cheeses = ["gouda", "brie", "cheddar"]
"brie" in cheeses   #should print True
"american" in cheeses   #should print False
"gouda" in cheeses  #should print True

#TRAVERSING A LIST
#the most common way to traverse a list is with the FOR loop, which follows similar syntax to strings:
for i in cheeses:
    print(i)

#to write to, or update, the elements in a list, you need indices
#a common way to do that is with RANGE and LEN functions:

for i in range(len(numbers)):       #len() returns number of elements in the list | range() returns a list of indices
    numbers[i] = numbers[i] * 2
    #each time i iterates through the list, it (i) gets the index of the next element
# ^ this doesn't seem to work, and I don't understand why

#you can CONCATENATE a list using the + operator:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(type(c))

#the multiplication operator can be used to repeat a list:
print([0]*4)    #putting in brackets here makes this a list, so it behaves differently
print(0*4)      #notice how it's not in brackets, so it's an equation and not a list
print([1, 2, 3] * 3)

#you can also SLICE a list to access certain elements
print(c[1:3])

#and since lists are mutable, it's often worth making a copy before making changes
#you cannot just use the assignment operator, because doing so just creates a reference to the old list, and your changes will back propogate as a result
#there are a COUPLE WAYS TO MAKE COPIES OF LISTS:
t = ["a", "b", "c", "d", "e", "f", "g"]
t2 = t.copy()   #built in method
print(t2)
#OR
t3 = t[:]   #slicing method
print(t3)
#OR
t4 = list(t)
print(t4)
t2[1:3] = ["x", "y"]
print(t)    #original list will be unchanged
print(t2)   #this list should replace b and c values with x and y

#Python provides methods to operate on lists
#you do not want to write these as practice = practice.sort(), because most list methods are void
#to ADD SOMETHING to a list, you use the APPEND method
practice = ["a", "b", "c"]
practice.append("d")    #adds "d" to end of list
print(practice)

#to append all of the elements in two lists, use the EXTEND method:
practice_2 = ["e", "f", "g", "h", "i", "j", "k"]
practice.extend(practice_2)
print(practice)     #now you'll have elements from practice and practice_2 put together

#it's worth noting that in the example above, it leaves practice_2 unmodified

#if you want to ARRANGE items in a list, you use the SORT method, which arranges from LOW TO HIGH
messy = ["t", "e", "q", "a", "h", "j", "o"]
print(messy)
messy.sort()
print(messy)    #worth noting that the sort method will irrevocably alter the order in the original list

#you can DELETE elements from a list in a couple different ways
#one way is to use the POP method, which keeps the removed element(s) in the new variable that you create for it
practice = ["a", "b", "c", "d"]
practice_2 = practice.pop(1)    #takes "b" out of practice, and puts it into practice_2
print(practice)     #prints original without b
print(practice_2)   #now this has the b

#if you don't need to keep the element(s), you can use the DEL operator:
practice = ["a", "b", "c", "d"]
del practice[1] #gets rid of element at one-eth index, which is b
print(practice) #original list minus b
#you could also make it a range:
del practice[1:3] #or
del practice[:]
#as always, the slice selects all elements UP TO, BUT NOT INCLUDING the second index (i.e. if you want to remove up for fourth element, specify 5)

#if you know the element(s) you want to remove, but not the index, you can use the REMOVE method
#however, remove method only takes one argument
practice = ["a", "b", "c", "d"]
practice.remove("c")
print(practice)

#there are a number of built in functions that can be used to quickly look through lists
#this obviates need to write your own FOR loops

numbers = [3, 41, 12, 9, 74, 15]
print(len(numbers))     #get list length
print(max(numbers))     #print largest number in list
print(min(numbers))     #print lowest number in list
print(sum(numbers))     #print total of all elements put together
print(sum(numbers)/len(numbers))    #print average value in list

#obviously, SUM only works on numbers
#the others work on other types of data that can be comparable

#you could recreate the above manually, like done before:
total = 0
count = 0
while True:
    user_input = input("Please enter a number:\n")
    if user_input == "done":
        break
    value = float(user_input)
    total = total + value
    count = count + 1
    average = total / count
print("Your average is:", average)

#however, this could more easily be accomplished with built in functions:
number_list = list()    #create an empty list
while True:
    user_input = input("Please enter a number:\n")
    if user_input == "done":
        break
    value = float(user_input)   #convert the value entered by user to floating point
    number_list.append(value)   #add the value entered by the user to the number list
average = sum(number_list) / len(number_list)
print("The average of the numbers you entered is:", average)

'''a string is a sequence of characters, and a list is a sequence of values
but a list of characters is not the same as a string
to convert from a string to a list of characters, you can use LIST'''

s = "spam"      #naturally creates a string
print(type(s))
t = list(s)     #leaves the string alone, but creates a new list with same values
print(t)
print(type(t))

'''however, when it pulls in that string, it treats each letter as it's own element'''
'''if you want to break a string into full words, you can use the SPLIT method'''
s = "pining for the fjords" #build a string
print(s)
print(type(s))
t = s.split()   #invoke a method so use dot notation
print(t)
print(type(t))

'''after you've used the split method to break a string into a list of words, you can use the index operator to look at specific words'''
print(t[2])

'''if needed, you can invoke split with a special argument called a DELIMITER
the delimiter specifies which characters to use as word boundaries
this can be helpful with oddly formatted data'''
example = "spam-spam-spam-gobbles-timmy"
print(example)
print(type(example))
fixed_example = example.split("-")
print(fixed_example)
print(type(fixed_example))

'''you can also write the delimiter as a variable, and inject that
this was how it was done in the text'''
example = "spam-spam-spam-gobbles-timmy"
print(example)
print(type(example))
delimiter = "-"
fixed_example = example.split(delimiter)
print(fixed_example)
print(type(fixed_example))

'''the inverse of split is JOIN, which is used to take a list of strings and concatenate the elements
join is a string method, so yuou invoke it on the delimiter and pass the list as a parameter
it's worth noting that this process TURNS A LIST INTO A STRING'''

example = ["oh", "no", "mr.", "bliss"]  #create the list
print(example)
print(type(example))
delimiter = " "     #basically saying "put the space in and bring together"
fixed_example = delimiter.join(example)     #start with the delimiter (i.e. what you want between the elements), and then add JOIN and pass in the variable
print(fixed_example)
print(type(fixed_example))

'''you could bring the whole thing together without spaces, by just passing in empty quotes'''

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

'''objects and values'''
'''there is a difference between how Python recognizes the 'sameness' in a string vs a line'''
a = "banana"
b = "banana"
print(a, b)
print(type(a))
print(a is b)   #will execute as TRUE
#in this example, Python only created one string object, and both a and b refere to it

'''but check out what happens when you create two lists with the same values....'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a, b)
print(type(a))
print(a is b)   #will execute as FALSE
#in this case, we would say the two lists are EQUIVALENT, because they have the same values, but they are not IDENTICAL, because they are not the same object
'''if two objects are identical, they are also equivalent...but if they are equivalent, they are not necessarily also identical
however, to take this a step further, you can link lists together, using a technique called ALIASING'''
a = [1, 2, 3]
b = a           #NOTE the order -> placing the new variable name first is key here
print(b is a)   #will now execute as TRUE
'''the association of a variable to an object is called a REFERENCE.
in the above example, there are two 'references' to the same object.
An object with more than one reference also has more than one name, so that is known as the object being aliased.
Important to NOTE: if the aliased object is mutable, changes made to one alias with affect the other(s).
while this can be helpful, it also opens up lots of possibilities of errors...so it's best to avoid aliasing when working with mutable objects.'''
#continuing with example above:
b[0] = 17
print(a)    #will not print [17, 2, 3]

'''list ARGUMENTS'''
'''when you pass a list to a function, the function gets a reference to the list
if the function modifies a list parameter, the caller sees the change'''
#here is an example:
def delete_head(i):
    del i[0]    #this will delete the first element in a list

#create sample list
letters = ["a", "b", "c"]
#invoke function
delete_head(letters)    #this should delete "a" from the list
print(letters)

'''what's IMPORTANT TO NOTE is that the deletion is back propagating
you don't need to create a new variable to house the altered list, because the original list was mutable'''

'''it is also IMPORTANT TO DISTINGUISH between operations that modify lists (as seen above), and those operations that create new lists
for example, the APPEND method modifies an existing list (as seen above), while the math operator + will create a new list'''
example = [1, 2]
example_2 = example.append(3)   #will add three to the list BUT NOT CREATE A NEW VARIABLE
#but it doesn't actually create a new variable called example_2....that's really freaking confusing
print(example)  #will show the added 3
print(example_2)    #will print None

'''another way to to write this function is to have it create a new variable'''
#goal here is to remove the head
letters = ["a", "b", "c"]

def head_gone(i):
    return i[1:]  #return everything except the head/the first element

new_letters = head_gone(letters)
print(new_letters)
