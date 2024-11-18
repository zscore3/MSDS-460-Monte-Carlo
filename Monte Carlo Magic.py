import random
import time

class Card:
    def __init__(self, name, typ, cost, power, ability):
        self.name = name
        self.typ = typ
        self.cost = cost
        self.power = power
        self.ability = ability

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_hand(self, hand_size):
        return self.cards[:hand_size]

def new_deck():
    cards = [
        Card("Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"),
        Card("Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"),
        Card("Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"),
        Card("Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"),
        Card("Hired Claw", "Creature", 1, 1, ""),
        Card("Hired Claw", "Creature", 1, 1, ""),
        Card("Hired Claw", "Creature", 1, 1, ""),
        Card("Hired Claw", "Creature", 1, 1, ""),
        Card("Slickshot Show-Off", "Creature", 2, 1, "haste"),
        Card("Slickshot Show-Off", "Creature", 2, 1, "haste"),
        Card("Slickshot Show-Off", "Creature", 2, 1, "haste"),
        Card("Slickshot Show-Off", "Creature", 2, 1, "haste"),
        Card("Emberheart Challenger", "Creature", 2, 2, "haste,prowess"),
        Card("Emberheart Challenger", "Creature", 2, 2, "haste,prowess"),
        Card("Emberheart Challenger", "Creature", 2, 2, "haste,prowess"),
        Card("Emberheart Challenger", "Creature", 2, 2, "haste,prowess"),
        Card("Sunspine Lynx", "Creature", 4, 5, ""),
        Card("Sunspine Lynx", "Creature", 4, 5, ""),
        Card("Sunspine Lynx", "Creature", 4, 5, ""),
        Card("Sunspine Lynx", "Creature", 4, 5, ""),
        Card("Shock", "Instant", 1, 2, ""),
        Card("Shock", "Instant", 1, 2, ""),
        Card("Shock", "Instant", 1, 2, ""),
        Card("Shock", "Instant", 1, 2, ""),
        Card("Monstrous Rage", "Instant", 1, 0, ""),
        Card("Monstrous Rage", "Instant", 1, 0, ""),
        Card("Monstrous Rage", "Instant", 1, 0, ""),
        Card("Monstrous Rage", "Instant", 1, 0, ""),
        Card("Lightning Strike", "Instant", 2, 3, ""),
        Card("Lightning Strike", "Instant", 2, 3, ""),
        Card("Lightning Strike", "Instant", 2, 3, ""),
        Card("Lightning Strike", "Instant", 2, 3, ""),
        Card("Urabrask’s Forge", "Artifact", 3, 1, ""),
        Card("Urabrask’s Forge", "Artifact", 3, 1, ""),
        Card("Urabrask’s Forge", "Artifact", 3, 1, ""),
        Card("Urabrask’s Forge", "Artifact", 3, 1, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mountain", "Land", 0, 0, ""),
        Card("Mishra’s Foundry", "Land", 0, 0, ""),
        Card("Mishra’s Foundry", "Land", 0, 0, ""),
        Card("Mishra’s Foundry", "Land", 0, 0, ""),
        Card("Mishra’s Foundry", "Land", 0, 0, ""),
        Card("Rockface Village", "Land", 0, 0, ""),
        Card("Rockface Village", "Land", 0, 0, ""),
        Card("Rockface Village", "Land", 0, 0, ""),
        Card("Rockface Village", "Land", 0, 0, ""),
    ]
    return Deck(cards)

def is_mulligan(hand):
    land_count = sum(1 for card in hand if card.typ == "Land")
    # Check for 0 lands or all lands
    return land_count == 0 or land_count == len(hand)

def calculate_damage(hand, lands):
    damage = 0
    for card in hand:
        if card.name == "Monastery Swiftspear":
            damage += 1
        elif card.name == "Hired Claw":
            damage += 1
        elif card.name == "Slickshot Show-Off":
            if lands >= 2:
                damage += 3
        elif card.name == "Emberheart Challenger":
            if lands >= 2:
                damage += 2
        elif card.name == "Sunspine Lynx":
            if lands >= 4:
                damage += 5
        elif card.name == "Shock":
            damage += 2
        elif card.name == "Monstrous Rage":
            damage += 2
        elif card.name == "Lightning Strike":
            if lands >= 2:
                damage += 3
        elif card.name == "Urabrask’s Forge":
            damage += 1
        elif card.name == "Mishra’s Foundry":
            if lands >= 2:
                damage += 2
    return damage

def simulate_game():
    deck = new_deck()
    deck.shuffle()
    hand_size = 7
    hand = deck.draw_hand(hand_size)
    
    # Simulate mulligans
    while is_mulligan(hand) and hand_size > 1:
        hand_size -= 1
        deck.shuffle()
        hand = deck.draw_hand(hand_size)
    
    deck.cards = deck.cards[hand_size:]
    turns = 0
    damage = 0
    lands = 0

    # Keep turns going until damage hits 20
    while damage < 20:
        turns += 1
        if len(deck.cards) > 0:
            # return the next item in the deck
            drawn_card = deck.cards.pop(0)
            hand.append(drawn_card)
        # Always play a land if available
        for i, card in enumerate(hand):
            if card.typ == "Land":
                lands += 1
                del hand[i]
                break
        damage += calculate_damage(hand, lands)
    return turns

def main():
    random.seed()
    total_turns = 0
    trial_sims = [1000, 10_000, 100_000]
    for num_trials in trial_sims:
        start_time = time.time()
        for _ in range(num_trials):
            turns = simulate_game()
            total_turns += turns
        end_time = time.time()
        duration = end_time - start_time
        average_turns = total_turns / num_trials
        print(f"Number of trials: {num_trials}")
        print(f"Average number of turns to win: {average_turns:.2f}")
        print(f"Total execution time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
