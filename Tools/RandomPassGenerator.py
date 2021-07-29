import random

version = '0.1'
low = ["karthic","jl","kk"]
up = ["KK","JL","KARTHIC"]
numbers = "0123456789"
# symbols = "*;/.,_-{}[]()"


all = low+up
length = 3

password = "".join(random.sample(all,length))

print(password)