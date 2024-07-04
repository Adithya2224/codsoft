import random
import string

def generate_password(length, complexity=1):
  """
    Below are the given Complexity levels for your password generation
    Complexity levels:
    1: Lowercase and uppercase letters, numbers, and symbols
    2: Lowercase and uppercase letters, numbers, symbols, and spaces
    3: Lowercase and uppercase letters, numbers, symbols, spaces, and dictionary words
  """

  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

  if complexity >= 2:
    characters += " "

  if complexity >= 3:
    with open("dictionary.txt", "r") as f:
      words = f.readlines()
      for word in words:
        characters += word.strip()

  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

def main():
  """Prompts the user to specify the desired length and complexity of the password and generates a random password of the specified length and complexity."""

  # Prompt for the user to specify the desired length of the password
  length = int(input("Enter the desired length of the password: "))

  # Prompt for the user to specify the desired complexity of the password
  complexity = int(input("Enter the desired complexity you need for the password (1-3): "))

  # Generating a password using the generate_password() function
  password = generate_password(length, complexity)

  # Display the generated password on the screen
  print("Generated password:", password)

if __name__ == "__main__":
  main()
