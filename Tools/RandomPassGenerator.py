import random

version = '0.1'
low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "*;/.,_-{}[]()"


all = low+up
length = 2
password = "".join(random.sample(all,length))


while True:
    if password == "Ac":
        break
    else:
        password = "".join(random.sample(all,length))
        print(password)
        

