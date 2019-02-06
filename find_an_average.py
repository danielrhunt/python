#find an average
'''create a function you can invoke to quickly find an average'''

#prompt a user for input:
count = 0
total = 0
while True:
    user_input = input("Please enter your numbers here (type 'done' or 'exit' when you're finished):\n")
    if user_input == "done" or user_input == "Done" or user_input == "exit" or user_input == "Exit":
        break
    value = float(user_input)
    total = total + value
    count = count + 1
    average = total / count
    #round to nearest hundreth
    answer = round(average, 3)
print("The average of the numbers you entered is:", answer)
