import random

version = '0.1'
low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "*;/.,_-{}[]()"


all = low
length = 6
password = "".join(random.sample(all,length))


while True:
    if password == "karthi":
        print(password)
        break
    else:
        password = "".join(random.sample(all,length))
        

