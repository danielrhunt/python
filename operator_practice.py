# #practicing with boolean logic
#
# print(5==5) #will print True
# print(5==6) #will print False
#
# comparison operators include:
# x != y #x does not equal y
# x > y #x is greater than y
# x < y #x is less than y
# x >= y #x is greater than or equal to y, need that order for operators
# x <= y #x is less than or equal to y, need that order
# x is y #x is the same as y (even more powerful than equal sign)
# x is not y #x is not the same as y (even more powerful than equal sign)
# x == y #x equals y
#
# #remember to not use a single "=", because that's the assignment operator!
#
# #logical operators
# #there are three logical operators: "and", "or", and "not"
# xy = 5
# if xy is 5 and xy > 3:
#     print("xy is more than 3")
#
# xyx = 6
# if xyx is 5 or xyx > 5:
#     print("xyx is more than five")
#
# yxy = 7
# if yxy is not 7 and yxy is 7:
#     print("I don't know, I'm just trying stuff here")

#conditionals and alternative execution
#writing  small program to prompt user for input of a number, and then determine if the number is odd or even
#uses the modulo
user_input = input("Please enter a number in numeric format:\n")
user_input = (int(user_input)) #convert the user input into an integer
if user_input % 2 == 0:    #this basically says if it's divisible by two with no remainder, meaning it's even
    print("The number you entered is even")
else:
    print("The number you enetered is odd")

#writing small program to run forever until user terminates, so use While
while True:
    user_input = input("Please enter a number in numeric format:\n")
    #by placing user input inside the While brackets, it prompts for user input every time through the loop
    #if didn't do this, it would keep the original user input and go into an infinite loop
    if user_input == "done":
        print("Okay, you're done.")
        break
    elif user_input == "Done":
        print("Okay, you're done.")
        break
    user_input = int(user_input)
    if user_input % 2 == 0:    #this basically says if it's divisible by two with no remainder, meaning it's even
        print("The number you entered is even")
        continue
    else:
        print("The number you enetered is odd")
        continue
