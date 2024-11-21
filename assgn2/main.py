import json
import os

# File paths
USER_FILE = "users.json"
QUESTIONS_FILE = "questions.json"

# Load questions
def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        print("Questions file not found!")
        return {}
    with open(QUESTIONS_FILE, "r") as file:
        return json.load(file)

# Load users
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            json.dump({}, file)
    with open(USER_FILE, "r") as file:
        return json.load(file)

# Save users
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

# Signup
def signup(users):
    print("\n--- Signup ---")
    username = input("Enter a username: ").strip()
    if username in users:
        print("Username already exists!")
        return None
    password = input("Enter a password: ").strip()
    users[username] = {"password": password, "score": 0}
    save_users(users)
    print("Signup successful! Please login to continue.")
    return None

# Login
def login(users):
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    print("Invalid username or password!")
    return None

# Quiz
def take_quiz(username, questions, users):
    print("\n--- Quiz Topics ---")
    for idx, topic in enumerate(questions.keys(), start=1):
        print(f"{idx}. {topic}")
    choice = int(input("Choose a topic (number): ").strip())
    topic = list(questions.keys())[choice - 1]
    print(f"\nSelected Topic: {topic}")
    score = 0
    for q_idx, q in enumerate(questions[topic], start=1):
        print(f"\nQuestion {q_idx}: {q['question']}")
        for i, opt in enumerate(q['options'], start=1):
            print(f"{i}. {opt}")
        answer_idx = int(input("Enter your answer (option number): ").strip())
        if q['options'][answer_idx - 1].lower() == q['answer'].lower():
            score += 1
            print("Correct answer!")
        else:
            print(f"Wrong answer! Correct answer: {q['answer']}")
            
    print(f"\nYour score: {score}/{len(questions[topic])}")
    users[username]["score"] += score
    save_users(users)


# Main menu
def main():
    users = load_users()
    questions = load_questions()
    if not questions:
        print("No questions available! Exiting...")
        return
    
    print("Welcome to the Quiz App!")
    username = None
    while not username:
        print("\n1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            username = login(users)
        elif choice == "2":
            signup(users)
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    while True:
        print("\n--- Main Menu ---")
        print("1. Take a Quiz")
        print("2. View Score")
        print("3. Logout")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            take_quiz(username, questions, users)
        elif choice == "2":
            print(f"Your total score: {users[username]['score']}")
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

main()
