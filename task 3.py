# Importing random.
import random

# setting up some replay of questions for users.
replies = {
    'wifi': 'WiFi is excellent across the campus.',
    'library': 'The library is closed today',
    'deadline': 'Your deadline has been extended by two days',
    'teacher': 'teacher will be there soon',
    'results': 'results will be out by next month',
    'lab': 'lab is closed today',
}
# setting up some random replay.
random_replies = ['Hmm', 'Oh, yes, I see', 'Tell me more']

# (checking email if user gives it correct must have @ after more than 2 word if correct return true if not than return
# false.)


def email_checker(email_address):
    """validates an email passed when called"""
    if email_address.count('@') == 1 and email_address.index('@') >= 2:
        return True
    else:
        return False

#  setting up  IF ELSE functions questions.


def get_reply(question):
    question = question.lower()
    if 'wifi' in question:
        print(f"{replies['wifi']}")
    elif 'library' in question:
        print(f"{replies['library']}")
    elif 'deadline' in question:
        print(f"{replies['deadline']}")
    elif 'teacher' in question:
        print(f"{replies['teacher']}")
    elif 'results' in question:
        print(f"{replies['results']}")
    elif 'lab' in question:
        print(f"{replies['lab']}")
    elif 'bye' in question or 'exit' in question:
        return 0
    else:
        print(f"{random.choice(random_replies)}")

# define main function and call it down.


def main():
    # for output layout.
    print("Welcome to pop chat\nOne of our operators will be pleased to help you today.")
    # These are random name that welcome users.
    operator_names = ["Janice", "Candice", "Karen", "Jennifer", "Florence"]
    # taking input from users.
    email_address = input("Please enter your Poppleton email address:")
    # checking email address.
    if email_checker(email_address):
        username = email_address[0:email_address.index('@')]
        # greeting user.
        print(f"\nHello,{username}! Thank you, and welcome to Pop Chat !")
        print(f"My name is {random.choice(operator_names)}, and it will be my pleasure to help you.")
        # if user input is true then
        while True:
            # taking questions as input.
            question = input()
            if get_reply(question) == 0:
                break
            # taking random numbers by using randint function from(0 to 10).
            if random.randint(0, 10) > 9:
                print("Network Error")
                break

    else:
        print("Invalid email id")
    return


# calling main function.
main()
