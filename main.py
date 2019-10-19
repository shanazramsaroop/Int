#Shanaz Ramsaroop
#This is program with many games

print("Welcome to my number game!")

print("Choose an option: ")
print(" 1) Math question ")
print(" 2) Print numbers ")
print(" 3) Guessing game ")
print(" 4) Exit")
result = int(input("I choose: "))

if result == 1:
    print("Math question!")
    print("What is the remainder if 103 is divided by 5?")
    answer1=int(input("Your answer = "))
    correctAnswer1=(103 % 5)
    if answer1==correctAnswer1:
        print("Correct! You are so smart!")
    else:
        print("Oops! Not quite right.")

elif result == 2:
    print("Print numbers!")
    number = int(input("Enter any number"))
    for x in range (number + 1):
        print(x)
        print("-")
        x += 1

elif result == 3:
    print("Guessing game!")
    guess = int(input("Guess any number between 1 and 10"))

    import random
    answer3 = random.randint(1,11)
    guesses = int()
    guesses = 0

    while (answer3 != guess):
        guesses += 1
        if guess < answer3:
            print("Too low! Try again. ")
        elif guess > answer3:
            print("Too high! Try again. ")
        elif guess < 1 or guess > 10:
            print("Invalid number. Try again. ")

        guess = int(input("Guess any number between 1 and 10"))

    print("Correct, it took you", guesses, "guesses.")






