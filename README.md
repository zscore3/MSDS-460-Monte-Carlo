# MSDS-460-Monte-Carlo

# What’s being studied?
Magic the Gathering - draws & plays to win a game with a limited number of cards.
# What are we comparing? 
Python vs Go 

# Summary
We're looking to simulate draws and mulligans (in which the first hand of cards drawn is replaced in the deck and a new hand is drawn with one fewer card) in a trading card game deck, with different hands and draws resulting in different "turns to wins," based on a limited number of cards and interactions between them. This is based on an infamous deck in Magic the Gathering called Mono-Red Aggro, which has been studied somewhat extensively due to its relative ease of access and simple-but-effective ethos of winning the game before other competing decks can interact with it effectively. Succinctly put, it is a set of 60 cards which are intended to, as much as possible, remove variables from the game.

We’re going to simulate the activity in both Python and Go, and use the same performance benchmarks as our behavior simulation, Memory and Execution speed.

# Breakdown

The win condition is to deal 20 points of damage as quickly as possible.

Each trial, the deck is shuffled (i.e. randomized), 7 cards are drawn from the top, and any mulligans can occur. A mulligan involves the deck being shuffled again, and one less card being drawn. So the first hand has 7 cards, the second has 6, the third has 5, and so on. Then, once any mulligans have finished, the player’s series of turns may commence. 

Each turn, a player first draws a card, then may play a single land if they have any in their hand (incrementing their land total by 1), and may “tap” lands in order to play other cards. A tapped land or creature cannot be tapped again until it has been untapped at the beginning of the next turn. All creatures then deal damage, after which any remaining lands may be tapped to play any remaining cards in hand. Finally, the turn ends and the next one begins with all tapped cards being untapped and the player drawing another card from the deck.

The cards below are frequently accompanied by keywords and notations. 
(#) indicates the number of cards of that type in the deck
(L) indicates the alphabetical character key associated with that card
"# cost" indicates how many lands are to be tapped to play the card
"# power" indicates how much damage the creature can do per turn
Haste indicates that the creature can deal damage the first turn it is played
Otherwise the creature can’t deal damage until the second turn it is played
Prowess indicates that the creature gains 1 power until the end of the turn whenever a noncreature spell is cast.
Land indicates that it can be tapped to play other cards

The Deck of 60 cards consists of the following:
- Creatures (20)
    - Monastery Swiftspear (4) (A)
         - 1 cost, 1 power, haste, prowess
    - Hired Claw (4) (B)
         - 1 cost, 1 power, 
         - for 2 cost can add 1 power once per turn if an opponent has lost life
    - Slickshot Show-Off (4) (C)
         - 2 cost, 1 power, haste, 
         - gets +2 power until end of turn when a noncreature card is played.
    - Emberheart Challenger (4) (D)
         - 2 cost, 2 power, haste, prowess
    - Sunspine Lynx (4) (E)
         - 4 cost, 5 power, deals damage equal to the number of land cards played
- Instants (12)
    - Shock (4) (F)
         - 1 cost
         - Deals 2 damage
    - Monstrous Rage (4) (G)
         - 1 cost
         - Select creature gets +2 power until end of turn
    - Lightning Strike (4) (H)
         - 2 cost
         - Deals 3 damage
- Artifacts (4)
    - Urabrask’s Forge (4) (I)
         - 3 cost
         - Deals 1 the first turn it is out, 2 the second, etc.
- Lands (24)
    - Mountain (16) (J)
         - Basic Land
    - Mishra’s Foundry (4) (K)
         - Land
         - For 2 cost, can deal 2 damage
         - For 1 cost and a tap, can make another Mishra’s Foundry deal 4 instead
    - Rockface Village (4) (L)
         - Land
         - For 1 cost and a tap, can give an Emberheart Challenger or Hired Claw get +1 power and gain haste until end of turn.

The deck could be described as a sequence of the following alphabetical characters:
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJJJJJJJJJJJJJKKKKLLLL


# Example:

Start by “shuffling” the deck: 
