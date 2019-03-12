#list exercise

#write a function called "middle" that takes a list and returns a new list
#have the new list contain all EXCEPT the first and last elements

def middle(t):
    del t[0]
    del t[-1]
    return(t)

example = [1, 2, 3, 4, 5]
print(middle(example))
