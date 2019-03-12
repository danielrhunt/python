#lists and functions

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
