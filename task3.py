from random import randint


def random_string(lst):
    return lst[randint(0, len(lst) - 1)]


def isemail(email, domain):
    if 0 > email.count("@") > 2:
        return False

    if len(getname(email)) < 2:
        return False

    if email[email.find("@"):] != domain:
        return False

    return True


def getname(email):
    name = email[0:email.find("@")]
    return name


def inword (sent, word):
    if word.lower() in sent.lower():
        return True

    else:
        return False


network = [True, True, True, True, True, True, True, True, True, False]
names = ["alice", "bob"]
words = ["bye", "exit"]
no_comebacks = ["sorry", "Cant, Understand"]
exit = False

print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email = input("Please enter your Poppleton email address:")

if isemail(email, "@pop.ac.uk"):
    print(f"Hi, {getname(email)}! Thank you, and Welcome to PopChat!")
    print(f"My name is {random_string(names)}, and it will be my pleasure to help you.")
    while True:
        sent = input("Enter string:")
        for word in words:
            if inword(sent, word):
                exit = True
                break

        if exit:
            break

        if not random_string(network):
            print("Network error")
            break

        elif inword(sent, "library" or "Library"):
            print("The library is closed today.")

        elif inword(sent, "WiFi" or "wifi"):
            print("WiFi is excellent across the campus.")

        elif inword(sent, "deadline" or "Deadline"):
            print("Your deadline has been extended by two working days.")

        else:
            print(random_string(no_comebacks))
else:
    print("This email is not valid")