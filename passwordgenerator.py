import random
import string

def randomize_password(password):
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

# Prompt the user for password length
password_length = int(input("Provide your desired password length: "))

# Prompt the user for character set preferences
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_punctuation = input("Include symbols? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

# Build the character set based on user preferences
characters = ""
if include_digits:
    characters += string.digits
if include_punctuation:
    characters += string.punctuation
if include_uppercase:
    characters += string.ascii_uppercase
if include_lowercase:
    characters += string.ascii_lowercase

if not characters:
    print("No character set selected. Please try again and select at least one character type.")
else:
    # Generate and print the password
    password = "".join(random.choice(characters) for _ in range(password_length))
    print(f"Password generated: {randomize_password(password)}")
