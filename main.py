import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Prompt the user for their guess
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    main()