#class poker
import random
import hands as hand

class poker:
	deck = []
	discard = []
	players = {} #id:hand
	playerval = {} #name:handval
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
			print "{}: {} ".format(player, " ".join(self.players[player]))
			self.playerval[player] = hand.handval(self.players[player])
		#print "playerval: {}".format(self.playerval)
		maxplayer = ''
		maxplayers = []
		maxval = 0
		for player in self.playerval:
			if self.playerval[player][0] > maxval:
				maxplayer = player
				maxval = self.playerval[player][0]

		for player in self.playerval:
			if self.playerval[player][0] == maxval:
				maxplayers.append(player)

		if len(maxplayers) > 1:
			#TODO resolve tie: look at which val is higher
			tiemaxp = ''
			tiemaxv = 0
			for player in maxplayers:
				if int(str(self.playerval[player][1]).lstrip('HSDC')) > tiemaxv:
					tiemaxv = int(str(self.playerval[player][1]).lstrip('HSDC')) 
					tiemaxp = player
			print "Winner: {} with {}".format(tiemaxp, self.playerval[tiemaxp][1])	
			return tiemaxp
			#print "Winner tie: {} with {}".format(" & ".join(maxplayers), handlookup(maxval))
		else:
			#print "Winner: {} with {}".format(maxplayer, self.playerval[maxplayer])
			print "Winner: {} with {}".format(maxplayer, handlookup(maxval))
			return maxplayer
		#need to see if there's a tie	
		#return random.choice(self.players.keys())
def handlookup(val):
	vals = ['high card', 'pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush', 'royal flush']
	return vals[val]
