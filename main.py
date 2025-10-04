from random import randint
import art


def check_answer( user_guess, actual_answer ):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print("You got it! The answer was {actual_answer}.")



def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

    if level == "easy":





print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


answer = randint(1, 100)



guess = int(input("Make a guess: "))

