#working on list methods

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
