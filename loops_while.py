#practice with loops

#the WHILE statement
#using "while" asks the statement to evaluate whether somethign is TRUE or FALSE, and execute while true
#the order of evaluation for while is:
    #evaluate whether the condition is true or false
    #if the condition is false, exit the while statement and continue executino of next statement (if present)
    #if (and while) the conditin is true, execute the body, and then go back to step one (evaluate if true or false)

n = 5
while n >= 0:        #while n is greater than zero
    print(n)        #print n (on a new line)
    n = n - 1       #then subtract one from n and start over
print("Blastoff!")  #after complete (i.e. when n is no longer greater than zero), exit loop and print "blastoff!"

#as seen here, the body of the loop should change the value of one (or more) variables so that the condition eventually becomes false
#if you don't specify an iteration variable (and set it to eventually terminate), you'll generate an infinite loop - which is bad!

#infinite loops and BREAK
#you can use a "break" statement to jump out of a loop
while True:
    user_input = input("Please type your name here:\n")
    if user_input == "done":
        break
    if user_input == "Done":
        break
    print("Hello,", user_input) #print "Hello" ad infinitum until user breaks out by typing "done"
print("Okay, now we're out of the loop.")    #print this statement once you've broken out of the loop (but not until then)

#the above is a commom way to write a loop, because it allows you to affirmatively stop a loop (vs. waiting for something to happen on it's own)
#sometimes in a loop you want to finish the current iteration, and immediately jump to next iteration
#in these cases, you'd use the CONTINUE statement, which skips to the next iteration without finishing the current iteration

while True:
    user_input_2 = input("Please enter a digit here:\n")
    if user_input_2[0] == "#":  #if first digit of user input is hash sign, basically just start over
        continue
    if user_input_2 == "done":
        print("Okay, you're done")
        break
    user_input_2 = int(user_input_2)    #convert from string to integer
    reason = (user_input_2 * 5)
    print(reason)
print("Loop is broken")
