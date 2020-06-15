import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[self.rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self):
		result = ''
		for card in self.deck:
			result = result + str(card) + ", "
		return result

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		self.shuffle()
		return self.deck[0]

class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += card.value
		self.adjust_for_ace

	def adjust_for_ace(self):
		for card in self.cards:
			if card.rank == 'Ace':
				self.aces += 1

class Chips:

	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet
		self.bet = 0

	def lose_bet(self):
		self.total -= self.bet
		self.bet = 0

def take_bet(player_chips):
	while True:
		try:
			result = int(input("Bitte Einsatz eingeben: "))
		except: 
			print('Falsche Eingabe!')
		else: 
			if result >= 0 and result <= player_chips.total:
				player_chips.bet = result
				print('Einsatz angenommen.')
				break
			else:
				print('Einsatz abgelehnt.')

def hit(deck, hand):
	# Karte ziehen
	card_draw = deck.deal()
	print(card_draw + " gezogen.")
	hand.add_card(card_draw)
	# Value aktualisieren
	






test_deck = Deck()
print(test_deck.deal())