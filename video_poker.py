import random
class game_driver(object):
	def __init__(self):
		self.score = 0
		self.choice = None
	def print_menu(self):
		self.choice = int(input("1: New Game\n 2: Play Again\n 3: Quit\n"))
	def print_menu2(self):
		self.choice = int(input("1: New Game\n 2: Play Again\n 3: Quit\n"))
		self.to_do()
	def to_do(self):
		if self.choice == 1:
			self.score = 0
			self.deal(5)
		elif self.choice == 2:
			self.deal(5)
		elif self.choice == 3:
			sys.exit("Good Bye")
class video_poker(game_driver):
	def __init__ (self):
		self.suits = ['spades','hearts','diamonds','clubs'] 
		self.ranks = [i for i in range(2,15)]
		self.cards = []
		self.shuffle()

		for suit in self.suits:
			for rank in self.ranks:
				card_ = Card(suit,rank)
				self.cards.append(card_)

	def shuffle(self):
 
		random.shuffle(self.cards)
	def deal(self,cards_num):
		to_deal = []
		while cards_num > 0 and len(self.cards) > 0:
			to_deal.append(self.cards.pop())
			cards_num = cards_num-1
		if len(self.cards) == 0:
			for suit in self.suits:
				for rank in self.ranks:
					card_ = Card(suit,rank)
					self.cards.append(card_)
		print(to_deal)
		inp = int(input("1: Keep hand\n 2: Replace cards\n "))
		if inp == 1:
			evaluate(to_deal)
		elif inp == 2:
			inp_ = input("Enter number of cards to replace seperated by a comma, with most-left card being 1")
			x = inp_.split(",")
			for card_n in x:
				to_deal.pop(card_n-1)
			while len(to_deal) < 5:
				to_deal.append(self.cards.pop())
				if len(self.cards) == 0:
					for suit in self.suits:
						for rank in self.ranks:
							card_ = Card(suit,rank)
							self.cards.append(card_)
			evaluate(to_deal)
	def get_suit(self,card_value):
		return card_value % 4

	def get_rank(self,card_value):
		return card_value % 13
	def evaluate(self,hand):
		suitDict = {}
		rankDict = {}
		straight,flush,straightflush,royalflush = False
		hand = sorted(hand)
		for card in hand:
			if not card.rank in rankDict:
				rankDict[card.rank] = 1
			else:
				rankDict[card.rank] += 1 
		
			if not card.suit in suitDict:
				suitDict[card.suit] = 1
			else:
				suitDict[card.suit] += 1 
		if (hand[4].rank - hand[0].rank == 4) and (len(hand) == 5): 
			straight = True
		elif len(suitDict.keys()) == 1:
			flush = True
		elif straight and flush:
			straightflush = True
		elif straightflush and hand[4].rank == 14:
			royalflush = True
		
		#Random choose a card.
##
   #  Suits are stored in each card as strings
  ##  suits = ['spades','hearts','diamonds','clubs'] 

	# Ranks are stored as integers. So the deck is represented as cards from 2 ... 53.
   ## ranks = [i for i in range(2,54)]

	# To get the integer value of a suit we do (in this case a 1):
   ## suit_val = suits.index("hearts")

	# The first 13 cards (integers 2 - 14) represent all the 'spades'
	# The next 13 cards (integers 15 - 28) represent all the 'hearts'
	# And so on ...

	# So even though we store the suit for a card in the object, we only 
	# need it's integer value. 

   ## card1 = Card('diamonds',11) # This is the jack of diamonds and becomes card (2,11) or (37).

	# We calculate the integer value:
 ##	  card_value = ((suits.index("diamonds") * 13) + rank)

	# How do we leverage this knowledge to start to calculate hands?


##
class Card(video_poker):
	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def __str__(self):
	#Create dictionary for face cards
		translate = {11:'Jack', 12:'Queen', 13:'King', 14: 'Ace'}
		r = self.rank
	#check for face card
		if r in [11, 12, 13, 14]:
			myrank = translate[r]
		else:
			myrank = str(r)
		return myrank + " of " + self.suit


	def __lt__(self, other):
		return( self.rank < other.getRank() )



