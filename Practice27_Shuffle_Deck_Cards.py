# shuffle Deck Cards 
# random is used to shuffle the cards

import random, itertools

deck = list(itertools.product(range(1,14),["Spade", "Heart", "Diamond", "Club"]))
print(deck)

# shuufflig the card

random.shuffle(deck)
print(deck)
for i in range(5):
    print(deck[i][0], "of", deck[i][1])