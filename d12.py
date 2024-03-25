import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ")
    ANSWER = random.randint(1, 100)
    GUESSES = 10 if difficulty == 'easy' else 5

    return ANSWER, GUESSES

def difficulty():


game_state = True
while game_state == True:
    ANSWER, GUESSES = start_game()

    while GUESSES > 0:
        print(f"You have {GUESSES} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > ANSWER:
            print("Too high, guess again.")
            GUESSES -= 1
        elif guess < ANSWER:
            print("Too low, guess again.")
            GUESSES -= 1
        else:
            print("Correct!")
            break

        if GUESSES == 0:
            print(f"You've run out of guesses. The number was {ANSWER}.")

    replay = input("Do you want to play again? Type 'y' for yes, 'n' for no: ")
    if replay.lower() == 'n':
        game_state = False
        print("Thanks for playing! Goodbye.")
