'''TUPLE ASSIGNMENTS'''

'''one of the unique features of Python language is the ability to have a tuple on the left side of an assignment statement
this allows you to assign more than one variable at a time, when the left side is a sequence'''

#here is a two element list (which is a SEQUENCE)
m = ["have", "fun"]
print(m)
print(type(m))

#now we can assign the first and second elements of the sequence to the variables x and y in a single statement
x, y = m    #this turns them from list into string
print(x)
print(type(x))  #string!
print(y)
print(type(y))  #string!

'''you can also SWAP VALUES using the tuple assignment'''
a, b = b, a

'''both sides of that statement are tuples
the number of variables on the left, and the number on the right, must be the same!!!
more generally, the RIGHT SIDE can be any kind of sequence (string, list, tuple)
for example, to SPLIT AN EMAIL ADDRESS into a user name and domain, you could write:'''

email_address = "monty@python.org"
print(email_address)
user_name, domain = email_address.split("@")
print(user_name)
print(domain)
print(type(domain))
