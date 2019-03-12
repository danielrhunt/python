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
