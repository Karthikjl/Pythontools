import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number : "))
    if user == number:
        print(f"you guessed correctly it's {number}")
        break
if user != number:
    print(f"your guess is incorrect the number is {number}")