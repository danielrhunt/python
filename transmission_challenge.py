#transmission challenge
gears = input("How many gears does a G37x have:\n")
try:
    gears = float(gears)
    if gears == 7.0:
        print("Yes, a G37x has seven gears in the transmission.")
    else:
        print("That is incorrect.  Please try again.")
except:
    print("Please enter your answer in a digital format.")
