#Shanaz Ramsaroop
#This is program with many games


def number1(answer1):
    correctAnswer1 = (103 % 5)
    while answer1 != correctAnswer1:
        print("Oops! Not quite right, try again. ")
        print("Enter 1 to try again. ")
        print("Enter 2 to select another game. ")
        selection = int(input())
        if selection == 1:
             answer1 = int(input("Your answer = "))

    print("Correct! You are so smart. ")


def number2(line):
    for x in range(line + 1):
        print(x)
        x += 1

def number3(guess):

    import random
    answer3 = random.randint(1, 11)
    guesses = int()
    guesses = 0

    while answer3 != guess:
        guesses += 1
        if guess < answer3:
            print("Too low! Try again. ")
        elif guess > answer3:
            print("Too high! Try again. ")
        elif guess < 1 or guess > 10:
            print("Invalid number. Try again. ")

        guess = int(input("Guess any number between 1 and 10"))

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
        line = int(input("Enter any number"))
        number2(line)
        main()

    #option 3
    elif result == 3:
        print("Guessing game!")
        guess = int(input("Guess any number between 1 and 10"))
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







