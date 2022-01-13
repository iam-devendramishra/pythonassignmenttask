# task 1.
print("\n                     STOP! WHO WOULD CROSS THE BRIDGE OF DEATH                                ")
print("                Must answer me these questions three, 'ere the other side he see.\n                           ")

# Asking user for input:
name = str(input("what is your name:"))

# checking if input name is arthur.
if name == "arthur":
    arthur = True
    if arthur:
        print("My liege! You may pass!")

# asking user to input their required quest:
else:
    quest = input("what do you seek")
    if "grail" in quest:

        # asking user to input their favourite color
        colour = input("what is your favourite color?")

        # checking if input colour Match with first letter of their name:
        if colour[0] == name[0]:
            print("you may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
