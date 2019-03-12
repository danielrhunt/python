#practice with Python...
def say_hi(a):
    if a == "english":
        return("Hi")
    elif a == "spanish":
        return("hola")
    elif a == "french":
        return("Bonjour")

x = input("What language do you speak?\n")
y = input("And what is your name?\n")
print(say_hi(x), y)
