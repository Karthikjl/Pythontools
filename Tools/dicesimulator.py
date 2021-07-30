import random

while True:
    print("""1.roll the dice\n2.exit""")
    user = int(input("What you want to do ? "))
    if user == 1:
        number = random.randint(1,6)
        print("The number of dice is %s\n"%number)
    else:
        break