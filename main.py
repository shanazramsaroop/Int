#Shanaz Ramsaroop
#This is program with number games


def number1(answer1):
    correctAnswer1 = (103 % 5)
    while answer1 != correctAnswer1:
        print("Oops! Not quite right. ")
        print("Enter 1 to try again. ")
        print("Enter 2 to select another game. ")
        selection = int(input())
        if selection == 1:
             answer1 = int(input("Your answer = "))

    print("Correct! You are so smart. ")


def number2(a, b):
    for x in range(a, b + 1):
        print(x)
        x += 1

def number3(guess):

    import random
    answer3 = random.randint(1, 20)
    guesses = int()
    guesses = 0

    while answer3 != guess:
        guesses += 1
        if guess < answer3:
            print("Too low! Try again. ")
        elif guess > answer3:
            print("Too high! Try again. ")
        elif guess < 1 or guess > 20:
            print("Invalid number. Try again. ")

        guess = int(input("Guess any number between 1 and 20"))

    print("Correct, it took you", guesses, "guesses.")


def number(result):

    #option 1
    if result == 1:
        print("Math question!")
        print("What is the remainder if 103 is divided by 5?")
        answer1 = int(input("Your answer = "))
        number1(answer1)
        main()

    #option 2
    elif result == 2:
        print("Print numbers!")
        print("Enter any  2 numbers")
        line1 = int(input("First number: "))
        line2 = int(input("Second number: "))
        number2(line1, line2)

        main()

    #option 3
    elif result == 3:
        print("Guessing game!")
        guess = int(input("Guess any number between 1 and 20"))
        number3(guess)
        main()

   #invalid number
    elif result > 4 or result < 1:
        print("Invalid number. Please enter a valid number. ")
        main()


def main():
    print("")
    print("Welcome to my number game!")
    print("Choose an option: ")
    print(" 1) Math question ")
    print(" 2) Print numbers ")
    print(" 3) Guessing game ")
    print(" 4) Exit")
    print("")
    result = int(input("I choose: "))
    number(result)


main()







