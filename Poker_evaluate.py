import collections
class Card():
	def __init__(self,x):
		self.rank = x[0]
		self.suit = x[1]
	def __eq__(self,other):
		if self.rank == other.rank and self.suit == other.suit:
			return True
		else:
			return 0
	def __lt__(self,other):
		if self.rank < other.rank:
			return 1
		else:
			return 0
if __name__ == '__main__':
	hand = []
	array = [(5,1),(8,2),(7,3),(6,4),(9,1)]
	for val in array:
		hand.append(Card(val))
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
	print(handval)
