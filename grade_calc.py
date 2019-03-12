#build a grade calculator
user_input_1 = input("Please enter your class grade in digit form: \n")
try:
    user_input = float(user_input_1)
    if user_input >= 1.1:
        print("That's not a valid score, asshole!")
    elif user_input >= 0.9:
        print("A")
    elif user_input >= 0.8:
        print("B")
    elif user_input >= 0.7:
        print("C")
    elif user_input >= 0.6:
        print("D")
    elif user_input < 0.6:
        print("You get an F!")
except:
    print("Please enter in digits only, between 0 and 1.0.")
