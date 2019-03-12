#counting for letters in a string
#counting number of times a letter appears in a string
word = "banana"
count = 0 #start from zero when counting
for i in word:
    if i == "a": #searching for letter "a"
        count = count + 1
print("The number of times the letter appears is:", count)
