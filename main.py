"""
__author__ = Shanaz Ramsaroop
 This is a program with number games
"""


def try_again1():
    """allows the user to try option 1 again or choose another game."""
    var_is_bad = True
    while var_is_bad:
        try:
            print("Enter 1 to try again.")
            print("Enter 2 to choose another game.")
            var = int(input())
            var_is_bad = False
            if var == 1:
                answer1 = input("Your answer = ")
                number1(answer1)
            elif var == 2:
                main()

        except ValueError:
            print("This is not a number.")
            print("Please enter a whole number.")


def number1(answer1):
    """
    tests if the inputted answer is correct or wrong and outputs text
    accordingly.
    :param answer1: answer for option 1
    """
    guess1 = 0

    while answer1 != "3" and guess1 == 0:
        guess1 += 1
        print("Oops! Not quite right. ")
        print("")
        try_again1()

    if answer1 == "3":
        print("Good job! You got it correct. ")
        print("")


def number2(a, b):
    """
    prints all the numbers from the first inputted number to the second
    inputted number.
    :param a: first number
    :param b: second number
    """

    if a > b:
        print("Sorry, the first number is larger than the second.")
        print("Please enter new numbers.")

    for x in range(a, b + 1):
        print(x)
        x += 1


def number3(guess):
    """
    tests if the guess is correct or wrong and outputs text accordingly.
    :param guess: answer for option 3
    """
    import random
    answer3 = random.randint(1, 20)
    guesses = 0
    if guess < 1 or guess > 20:
        print("Invalid number. Try again. ")
        number(3)

    while answer3 != guess and guesses <= 5:
        guesses += 1
        if guess < answer3:
            print("Too low! Try again. ")
        elif guess > answer3:
            print("Too high! Try again. ")

        attempts = 5 - guesses

        if guesses <= 5:
            print("Number of attempts left =", attempts)
            guess = int(input("Guess any number between 1 and 20"))
        elif guesses > 5:
            print("Sorry, you ran out of attempts.")

    if guesses == 0:
        print("You got it on the first try, good guess!")

    elif guesses == 1:
        print("Correct, it took you just two guesses!")

    elif guesses < 5:
        print("Correct, it took you", guesses, "guesses.")

    elif guesses == 5:
        print("Close one! You nearly ran out of guesses!")


def number(result):
    """
    Takes the user's input and sorts it to the appropriate gaming option or
    indicates the invalidity of the input.
    :param result: user's choice from menu
    """

    # option 1
    if result == 1:
        print("")
        print("Math question!")
        print("What is the remainder if 103 is divided by 5?")
        print("")
        answer1 = input("Your answer = ")
        number1(answer1)
        main()

    # option 2
    elif result == 2:
        print("")
        print("Print numbers!")
        print("Enter any  2 numbers, BUT the first number must be smaller "
              "than the second number.")
        print("")
        line1_is_bad = True
        line2_is_bad = True
        while line1_is_bad or line2_is_bad:
            try:
                line1 = int(input("First number: "))
                line2 = int(input("Second number: "))
                line1_is_bad = False
                line2_is_bad = False
                number2(line1, line2)

            except ValueError:
                print("This is not a number.")
                print("Please enter a whole number.")
                number(2)
        main()

    # option 3
    elif result == 3:
        print("")
        print("Guessing game!")
        print("")
        guess_is_bad = True
        while guess_is_bad:
            try:
                guess = int(
                    input("You have five guesses to guess a number between 1 "
                          "and 20"))
                guess_is_bad = False
                number3(guess)

            except ValueError:
                print("This is not a number.")
                print("Please enter a whole number.")
                number(3)
        main()

    # invalid number
    elif result > 4 or result < 1:
        print("")
        print("Invalid number. Please enter a valid number. ")
        print("")
        main()

    elif result == 4:
        print("Bye!")


def main():
    """This is the menu, where users can choose which game they want to play
    or exit."""
    print("")
    print("Welcome to my number game!")
    print("")
    print("Choose an option: ")
    print(" 1) Math question ")
    print(" 2) Print numbers ")
    print(" 3) Guessing game ")
    print(" 4) Exit")
    print("")
    result_is_bad = True
    while result_is_bad:
        try:
            result = int(input("Your choice: "))
            result_is_bad = False
            number(result)

        except ValueError:
            print("This is not a number.")
            print("Please enter a whole number.")


main()
