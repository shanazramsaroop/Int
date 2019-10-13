#Shanaz Ramsaroop
#This is a fun trvia game

print("Hello, welcome to my exciting trivia game. Hope you have fun!")
print("Number 1: What is the remainder if 103 is divided by 5?")
answer1=int(input("Your answer = "))
correctAnswer1=(103 % 5)
if answer1==correctAnswer1:
    print("Correct! You are so smart!")
else:
    print("Oops! Not quite right.")

print("Number 2: The cost of 2 phones and 3 airpods is $750, and the cost of 3 phone and 5 airpods $1150."
      " How much does 2 airpods cost? ")
print("Choose an answer")
print("a. $50")
print("b. $120")
print("c. $100")
print("d. $80")
answer2=str(input("Your answer: "))
if answer2 == "c":
    print("Correct! You are so smart!")
else:
    print("Oops! Not quite right.")
