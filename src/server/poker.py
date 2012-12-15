#class poker
import random
import hands as hand

class poker:
	deck = []
	discard = []
	players = {} #id:hand

	def __init__(self):
		self.deck = ['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ] #initialize
		
	def shuffle(self):
		random.shuffle(self.deck)

	def registerPlayer(self,player):
		if len(self.players) > 4:
			print "too many players"
		self.players[player] = []

	def deal(self,player):
		hand = []
		if player in self.players.keys():
			for i in range(0,5):
				hand.append(self.deck.pop())
			self.players[player] = hand
		else:
			print "player not found."
		return list(hand)

	def swap(self, player, cards):
		#send back as many as in cards
		hand = []
		if player in self.players.keys():
			for card in cards:
				if card in self.players[player]:
					if len(self.deck) < len(cards)+1 :
						print "error: not enough deck remaining!"
						exit(-1) #TODO discard
				else:
					print "error: cards not in player's hand! player: {} hand: {} cards: {}".format(player, " ".join(self.players[player]), " ".join(cards))
			for i in range(0,len(cards)):
				hand.append(self.deck.pop())
				#swap out cards
			for card in cards:
				self.players[player].remove(card)
			self.players[player].extend(hand)
		else:
			print "error: player not found"
		return list(hand)

	def resolve(self):
		# return which player has the higher hand
		for player in self.players:
			print "player: {} hand: {} ".format(player, " ".join(self.players[player]))
			if hand.isroyalflush(self.players[player]) != '00':
				print "{} has a royal flush!".format(player)
			if hand.isstraightflush(self.players[player]) != '00':
				print "{} has a straight flush!".format(player)
			if hand.isfourofakind(self.players[player]):
				print "{} has four of a kind!".format(player)
			if hand.isfullhouse(self.players[player]):
				print "{} has a full house!".format(player)
			if hand.isflush(self.players[player]) != '0':
				print "{} has a flush!".format(player)
			if hand.isstraight(self.players[player]):
				print "{} has a straight!".format(player)
			if hand.isthreeofakind(self.players[player]):
				print "{} has a three of a kind!".format(player)
			if hand.istwopair(self.players[player]):
				print "{} has two pairs!".format(player)
			if hand.ispair(self.players[player]):
				print "{} has a pair!".format(player)

		#return random.choice(self.players.keys())