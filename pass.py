import string
import random

# Function to get user input and validate it is a non-negative number
def get_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                print("Your number should be non-negative.")
            else:
                return user_input
        except ValueError:
            print("Please enter numbers only.")

def generate_password():
    print("Welcome to Password Generator")

    # Ask user about the number of characters
    num_letters = get_input("How many letters do you want in your pass? ")
    num_numbers = get_input("How many numbers do you want in your pass? ")
    num_symbols = get_input("How many symbols do you want in your pass? ")

    # Using random.choices() to allow repetition
    password_characters = (
        random.choices(string.ascii_letters, k=num_letters) +
        random.choices(string.digits, k=num_numbers) +
        random.choices(string.punctuation, k=num_symbols)
    )

    # Shuffle and join to create the password
    random.shuffle(password_characters)
    password = ''.join(password_characters)

    return password

# List to store generated passwords
passwords_list = []

# Generate and store password
password = generate_password()
passwords_list.append(password)

# Output the generated password
print('This is your password:', password)

