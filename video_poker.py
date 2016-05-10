import random
import collections
class Card(object):
	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit
	def __repr__(self):
		translate = {11:'Jack', 12:'Queen', 13:'King', 14: 'Ace'}
		r = self.rank
		if r in [11, 12, 13, 14]:
			myrank = translate[r]
		else:
			myrank = str(r)
		return( myrank + " of " + self.suit)

	def __eq__(self,other):
		if self.rank == other.getRank() and self.suit == other.getSuit():
			return True
		else:
			return 0
	def __lt__(self,other):
		if self.rank < other.getRank():
			return 1
		else:
			return 0
class video_poker(Card):
	def __init__ (self):
		self.suits = ['spades','hearts','diamonds','clubs'] 
		self.ranks = [i for i in range(2,15)]
		self.cards = []
		self.restock()
	def shuffle(self):
		random.shuffle(self.cards)
	def deal(self,cards_num):
		bla=cards_num
		to_deal = []
		while bla > 0:
			to_deal.append(self.cards.pop())
			bla -=1
			if len(self.cards) <=1:
				self.restock()
		
		print(to_deal)
		inp = int(input(" 1: Keep hand\n 2: Replace cards\n "))
		if inp == 1:
			self.evaluate(to_deal)
			
		elif inp == 2:
			inp_ = input("Enter number of cards to replace seperated by a comma, begining with the biggest card Number 5(most-right)  ")
			x = inp_.split(",")
			for card_n in x:
				to_deal.pop(int(card_n)-1)
			while len(to_deal) < 5:
				to_deal.append(self.cards.pop())
				if len(self.cards) <=1:
					self.restock()
			print(to_deal)
			self.evaluate(to_deal)
	def restock(self):
		for suit in self.suits:
			for rank in self.ranks:
				card_ = Card(suit,rank)
				self.cards.append(card_)
		random.shuffle(self.cards)
	def __str__(self):
		if type(self)==list:
			for v in self:
				print(v)



	def evaluate(self,hand):
		score = 0
		hand.sort()
		suitDict = collections.defaultdict(int)
		rankDict = collections.defaultdict(int)
		handval = ""
		straight = False
		flush = False
		straightflush = False
		for card in hand:
			rankDict[card.rank] += 1 
			suitDict[card.suit] += 1 
		if (hand[4].rank - hand[0].rank == 4) and (len(hand) == 5): 
			straight = True
			handval ="Straight !"
			score = 4
			print (hand)
		if len(suitDict) == 1:
			flush = True
			handval ="Flush !"
			score = 5
		if straight and flush:
			straightflush = True
			score = 50
			handval ="Straight Flush !"
		if straightflush and hand[4].rank == 14:
			score = 800
			handval ="Royal Flush !"
		if len(rankDict) == 4:
			handval ="One Pair !"
			score = 1
		elif len(rankDict) == 3:
			if 3 in rankDict.values():
				handval ="Three of a Kind !"
				score = 3
			else:
				score = 2
				handval = "Two Pairs !"
		elif len(rankDict) ==2:
			x = list(rankDict.values())
			a = list(rankDict.keys())
			if x[0] == 1 :
				four = a[1]
				handval = "Four of a Kind of " + str(four)
				score = 25
				if int(four) ==8:
					score = 80
				elif int(four) == 7:
					score = 50
			elif x[1] == 1:
				four = a[0]
				handval = "Four of a Kind of " + str(four)
				score = 25
				if int(four) ==8:
					score = 80
				elif int(four) == 7:
					score = 50
			else:
				handval = "Full House !"
				score = 8
		else:
			handval = "Loser !"
			self.score = 0
		print(handval)
		print("This hand gets you " + str(score))
		game_driver.get_score(self,score)
		game_driver.print_menu2(self)

class game_driver(video_poker,Card):
	def __init__(self):
		self.score = 0
		self.choice = None
		super().__init__()
	def get_score(self, num):
		self.score = num
	def print_menu(self):
		self.choice = int(input(" 1: New Game\n 2: Play Again\n 3: Quit\n"))
	def print_menu2(self):
		print("Total Score :" + str(self.score))
		self.choice = int(input(" 1: New Game\n 2: Play Again\n 3: Quit\n"))
		self.to_do()
	def to_do(self):
		if self.choice == 1:
			self.score = 0
			print("Score :" + str(self.score))
			self.deal(5)
		elif self.choice == 2:
			print("Score :" + str(self.score))
			self.deal(5)
		elif self.choice == 3:
			sys.exit("Good Bye")



if __name__ == '__main__':
	game = game_driver()
	game.print_menu()
	game.deal(5)
