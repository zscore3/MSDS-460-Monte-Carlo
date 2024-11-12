import random
import itertools


# Create and Shuffle the Deck
DECK = tuple('AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJJJJJJJJJJJJJKKKKLLLL')
SHUFFLE_DECK = list(DECK)
random.shuffle(SHUFFLE_DECK)
#print(SHUFFLE_DECK)

# Draw the first 7 cards from the top of the deck into your hand
N = 7
HAND = SHUFFLE_DECK[:N]
#print(HAND)


