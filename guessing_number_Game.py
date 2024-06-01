import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses allowed
max_guesses = 10

# Initialize the number of guesses made
guesses_made = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} guesses to get it right.")

# Game loop
while guesses_made < max_guesses:
    # Get the user's guess
    guess = int(input("Your guess: "))
    
    # Increment the number of guesses made
    guesses_made += 1
    
    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {guesses_made} guesses.")
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

# If the user runs out of guesses
if guesses_made == max_guesses:
    print(f"Sorry, you didn't guess the number. The number was {secret_number}.")