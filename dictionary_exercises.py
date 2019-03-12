#dictionary exercise
words = dict()  #create empty dictionary
document = open("words.txt")
for i in document:
    boom = i.split()
    i = i.rstrip()
    print(i)
