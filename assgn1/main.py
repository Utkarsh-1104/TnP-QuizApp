print('-'*40)
print('Welcome to Quiz Game')
print('-'*40)

# Importing the questions from the questions.py file
from quizData import topics
print(topics[0]['data'][0])

users = {}

def startQuiz():
    score = 0
    i = 1
    for topic in topics:
        print(f'Press {i} to choose {topic["topic"]}')
        i += 1
    choice = int(input("Enter your choice: "))
    questions = topics[choice - 1]["data"]
    for question in questions:
        print("-"*40)
        print(question["question"])
        for index, option in enumerate(question["options"]):
            print(f'{index + 1}. {option}')
        answer = int(input("Enter your answer: "))
        if (question["options"][answer - 1] == question["answer"]):
            score += 1
            print("Correct answer")
        else:
            print("Wrong answer")
            print("Correct answer is", question["answer"])
    print(f'Your score is {score}/{len(questions)}')


def playGame():
    startQuiz()
    playAgain = input("Do you want to play again? (yes/no): ")
    if (playAgain == "yes"):
        startQuiz()
    else:
        print("Thank you for playing")


def signIn():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if (username in users.keys() and users[username] == password):
        print("You have successfully signed in")
        print("-"*40)
        startQuiz()
    else:
        print("Invalid username or password")
        authenticate()

def signUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users[username] = password
    print("You have successfully signed up")
    print("-"*40)
    playGame()

def authenticate():
    print("Press 1 to sign in")
    print("Press 2 to sign up")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        signIn()
    else:
        signUp()

authenticate()