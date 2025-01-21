from random import choice as cs 
import random

# Imports from libraries. 
# random.choice() choose a random element from the list.
# random.randint(from, to) generates a random integer between from and to parameter.
# random.shuffle(list) shuffles the elements of list.



# coin = random.choice(["heads" , "tails"])
# coin = cs(["heads" , "tails"])
# print(coin)


# number = random.randint(1,100)
# print(number)


cards = ["jack", "king" , "queen", "diamond", "heart", "club", "spade"]
random.shuffle(cards)

for crd in cards :
    print(crd)