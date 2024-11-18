package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Card struct {
	name    string
	typ     string
	cost    int
	power   int
	ability string
}

type Deck struct {
	cards []Card
}

func (d *Deck) shuffle() {
	rand.Shuffle(len(d.cards), func(i, j int) {
		d.cards[i], d.cards[j] = d.cards[j], d.cards[i]
	})
}

func (d *Deck) drawHand(handSize int) []Card {
	return d.cards[:handSize]
}

func newDeck() *Deck {
	cards := []Card{
		{"Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"},
		{"Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"},
		{"Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"},
		{"Monastery Swiftspear", "Creature", 1, 1, "haste,prowess"},
		{"Hired Claw", "Creature", 1, 1, ""},
		{"Hired Claw", "Creature", 1, 1, ""},
		{"Hired Claw", "Creature", 1, 1, ""},
		{"Hired Claw", "Creature", 1, 1, ""},
		{"Slickshot Show-Off", "Creature", 2, 1, "haste"},
		{"Slickshot Show-Off", "Creature", 2, 1, "haste"},
		{"Slickshot Show-Off", "Creature", 2, 1, "haste"},
		{"Slickshot Show-Off", "Creature", 2, 1, "haste"},
		{"Emberheart Challenger", "Creature", 2, 2, "haste,prowess"},
		{"Emberheart Challenger", "Creature", 2, 2, "haste,prowess"},
		{"Emberheart Challenger", "Creature", 2, 2, "haste,prowess"},
		{"Emberheart Challenger", "Creature", 2, 2, "haste,prowess"},
		{"Sunspine Lynx", "Creature", 4, 5, ""},
		{"Sunspine Lynx", "Creature", 4, 5, ""},
		{"Sunspine Lynx", "Creature", 4, 5, ""},
		{"Sunspine Lynx", "Creature", 4, 5, ""},
		{"Shock", "Instant", 1, 2, ""},
		{"Shock", "Instant", 1, 2, ""},
		{"Shock", "Instant", 1, 2, ""},
		{"Shock", "Instant", 1, 2, ""},
		{"Monstrous Rage", "Instant", 1, 0, ""},
		{"Monstrous Rage", "Instant", 1, 0, ""},
		{"Monstrous Rage", "Instant", 1, 0, ""},
		{"Monstrous Rage", "Instant", 1, 0, ""},
		{"Lightning Strike", "Instant", 2, 3, ""},
		{"Lightning Strike", "Instant", 2, 3, ""},
		{"Lightning Strike", "Instant", 2, 3, ""},
		{"Lightning Strike", "Instant", 2, 3, ""},
		{"Urabrask’s Forge", "Artifact", 3, 1, ""},
		{"Urabrask’s Forge", "Artifact", 3, 1, ""},
		{"Urabrask’s Forge", "Artifact", 3, 1, ""},
		{"Urabrask’s Forge", "Artifact", 3, 1, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mountain", "Land", 0, 0, ""},
		{"Mishra’s Foundry", "Land", 0, 0, ""},
		{"Mishra’s Foundry", "Land", 0, 0, ""},
		{"Mishra’s Foundry", "Land", 0, 0, ""},
		{"Mishra’s Foundry", "Land", 0, 0, ""},
		{"Rockface Village", "Land", 0, 0, ""},
		{"Rockface Village", "Land", 0, 0, ""},
		{"Rockface Village", "Land", 0, 0, ""},
		{"Rockface Village", "Land", 0, 0, ""},
	}
	return &Deck{cards: cards}
}

func simulateGame() int {
	deck := newDeck()
	deck.shuffle()
	handSize := 7
	hand := deck.drawHand(handSize)

	// Simulate mulligans
	for isMulligan(hand) && handSize > 1 {
		handSize--
		deck.shuffle()
		hand = deck.drawHand(handSize)
	}

	deck.cards = deck.cards[handSize:]

	turns := 0
	damage := 0
	lands := 0
	// keep turns going until damage hits 20
	for damage < 20 {
		turns++
		if len(deck.cards) > 0 {
			drawnCard := deck.cards[0]
			deck.cards = deck.cards[1:]
			hand = append(hand, drawnCard)
		}

		// always play a land if available
		for i, card := range hand {
			if card.typ == "Land" {
				lands++
				hand = append(hand[:i], hand[i+1:]...)
				break
			}
		}
		damage += calculateDamage(hand, lands)
	}

	return turns
}

func isMulligan(hand []Card) bool {
	landCount := 0
	for _, card := range hand {
		if card.typ == "Land" {
			landCount++
		}
	}
	// check for 0 lands or all lands
	return landCount == 0 || landCount == len(hand)
}

func calculateDamage(hand []Card, lands int) int {
	damage := 0
	for _, card := range hand {
		switch card.name {
		case "Monastery Swiftspear":
			damage += 1
		case "Hired Claw":
			damage += 1
		case "Slickshot Show-Off":
			if lands >= 2 {
				damage += 3
			}
		case "Emberheart Challenger":
			if lands >= 2 {
				damage += 2
			}
		case "Sunspine Lynx":
			if lands >= 4 {
				damage += 5
			}
		case "Shock":
			damage += 2
		case "Monstrous Rage":
			damage += 2
		case "Lightning Strike":
			if lands >= 2 {
				damage += 3
			}
		case "Urabrask’s Forge":
			damage += 1
		case "Mishra’s Foundry":
			if lands >= 2 {
				damage += 2
			}
		}
	}
	return damage
}

func main() {
	rand.New(rand.NewSource(0))
	totalTurns := 0
	trialSims := []int{1000, 10000, 100000}

	for _, numTrials := range trialSims {
		startTime := time.Now()
		for i := 0; i < numTrials; i++ {
			turns := simulateGame()
			totalTurns += turns
		}
		avgTurns := float64(totalTurns) / float64(numTrials)
		endTime := time.Now()
		duration := endTime.Sub(startTime)
		fmt.Printf("Number of Trials: %d\n", numTrials)
		fmt.Printf("Average number of turns to win: %.2f\n", avgTurns)
		fmt.Printf("Total execution time: %v\n", duration)
	}
}
