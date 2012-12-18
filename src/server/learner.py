# learner.py
# keeps a list of states it's seen
#	should states be actual cards in hand (sorted, HSDC 1-14)
#	or just as representation?
#		sorted hand. 
#		so we need a 'possible swaps' expansion
#
# * determine best action: 
#	- use laplace smoothing for estimates
#	for each set of possible swaps (choose1, choose2, choose3):
#		% of possible hands w/higher value
#		% of possible hands w/same or lower val
#		results we've seen at each of these (W or L)
# * list best action
#
# * make exploration/exploitation determination.     
import random
import hands
class learner:
	hand = []
	learnerid = 'learner'	
	store = 'learner.txt'
	learnedvals = {}
	def __init__(self,inhand):
		self.hand = inhand
		self.sorthand()
		self.initcounts()

	def initcounts(self):
		#open learner
		#count how many wins and losses for each val we get
		#split on :  then line[1] chop () split on ,   [0] is handval   line[2] is W or L (count T as L)
		for i in range(0,10):
			self.learnedvals[i] = [0,0]

		with open(self.store, 'r') as s:
			for line in s:
				cols = line.strip().split(":")
				handval = int(cols[1].strip("()").split(",")[0])
				winval = 0
				if cols[2] == 'W':
					winval = 1
				self.learnedvals[handval][winval] += 1
				#print "{}:{}".format(handval,cols[2]	)
		#so then we have a struct of learnedvals[handval]->[#W,#L]
		#for keys in self.learnedvals:
		#	print "handval:{} wins:{} losses:{}".format(keys, self.learnedvals[keys][1], self.learnedvals[keys][0])
		
	def sorthand(self):
		lookup=['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ]
		sample = sorted(self.hand, key=lambda x: lookup.index(x))	
		self.hand = list(sample)

	def highervals1(self, hand):
		deck=['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ]
		#should remove the current hand
		for card in hand:
			deck.remove(card)
		currval = hands.handval(hand)[0]
		cardremoves = {}
		for currcarda in hand:
			highercount = lowercount = samecount = 0
			ahand = list(hand)
			ahand.remove(currcarda)
			for carda in deck:
				adeck = list(deck)
				adeck.remove(carda)
				testhand = list(ahand)
				testhand.append(carda)
				tempval = hands.handval(testhand)[0]
				wins = self.learnedvals[tempval][1]
				losses = self.learnedvals[tempval][0]
				winlike = float(wins+1 ) / (wins + losses+2)
				#print "likelihood of win with {} is {}".format(tempval, winlike)
				if tempval > currval:
					highercount += 1.0*winlike
				elif currval > tempval: 
					lowercount += 1.0*winlike
				else:
					samecount += 1.0*winlike
			#print "lowercount:{} highercount:{} samecount:{}".format(lowercount,highercount,samecount)
			likelihigh =float (highercount) / (highercount+lowercount+samecount)	
			likelisame=float (samecount) / (highercount+lowercount+samecount)	
			likelilow=float (lowercount) / (highercount+lowercount+samecount)	
			#print "currcard:{} likelihood of higher:{} lower:{} same:{}".format(currcarda,likelihigh,likelilow,likelisame)
			cardremoves[currcarda] = likelihigh
		maxcard = ''
		maxval = 0.0
		for card in cardremoves:
			if cardremoves[card] > maxval:
				maxcard = card
				maxval = cardremoves[card]
		return (maxval, [maxcard])

	def highervals2(self, hand):
		deck=['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ]
		for card in hand:
			deck.remove(card)
		currval = hands.handval(hand)[0]
		cardremoves = {}
		ahand = list(hand)
		for currcarda in hand:
			cardremoves[currcarda] = {}
			ahand.remove(currcarda)
			for currcardb in ahand:
				highercount = lowercount = samecount = 0
				bhand = list(ahand)
				bhand.remove(currcardb)
				adeck = list(deck)
				for carda in deck:
					adeck.remove(carda)
					for cardb in adeck:
						testhand = list(bhand)
						testhand.append(carda)
						testhand.append(cardb)
						tempval = hands.handval(testhand)[0]
						wins = self.learnedvals[tempval][1]
						losses = self.learnedvals[tempval][0]
						winlike = float(wins+1 ) / (wins + losses+2)
						#print "likelihood of win with {} is {}".format(tempval, float(wins+1 ) / (wins + losses+2))
						if tempval > currval:
							highercount += 1.0*winlike
						elif currval > tempval: 
							lowercount += 1.0*winlike
						else:
							samecount += 1.0*winlike
				#print "lowercount:{} highercount:{} samecount:{}".format(lowercount,highercount,samecount)
				likelihigh =float (highercount) / (highercount+lowercount+samecount)	
				likelisame=float (samecount) / (highercount+lowercount+samecount)	
				likelilow=float (lowercount) / (highercount+lowercount+samecount)	
				#print "carda:{} cardb:{} likelihood of higher:{} lower:{} same:{}".format(currcarda,currcardb,likelihigh,likelilow,likelisame)
				cardremoves[currcarda][currcardb] = likelihigh
		maxval = 0.0
		maxcards= []
		for acard in cardremoves:
			for bcard in cardremoves[acard]:
				if maxval < cardremoves[acard][bcard]:
					maxval =cardremoves[acard][bcard]
					maxcards = [acard,bcard]	
				#print "acard:{} bcard:{} likelihood:{}".format(acard,bcard,cardremoves[acard][bcard])
		return (maxval, maxcards)
		#return likelihigh

	def highervals3(self, hand):
		deck=['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ]
		for card in hand:
			deck.remove(card)
		currval = hands.handval(hand)[0]
		cardremoves = {}
		ahand = list(hand)
		for currcarda in hand:
			cardremoves[currcarda] = {}
			ahand.remove(currcarda)
			for currcardb in ahand:
				bhand = list(ahand)
				bhand.remove(currcardb)
				cardremoves[currcarda][currcardb] = {}
				for currcardc in bhand:
					chand = list(bhand)
					chand.remove(currcardc)
					highercount = lowercount = samecount = 0
					adeck = list(deck)
					for carda in deck:
						adeck.remove(carda)
						bdeck = list(adeck)
						for cardb in bdeck:
							bdeck.remove(cardb)
							for cardc in bdeck:
								testhand = list(bhand)
								testhand.append(carda)
								testhand.append(cardb)
								testhand.append(cardc)
								tempval = hands.handval(testhand)[0]
								wins = self.learnedvals[tempval][1]
								losses = self.learnedvals[tempval][0]
								winlike = float(wins+1 ) / (wins + losses+2)
								#print "likelihood of win with {} is {}".format(tempval, float(wins+1 ) / (wins + losses+2))
								if tempval > currval:
									highercount += 1.0*winlike
								elif currval > tempval: 
									lowercount += 1.0*winlike
								else:
									samecount += 1.0*winlike
					#print "lowercount:{} highercount:{} samecount:{}".format(lowercount,highercount,samecount)
					likelihigh =float (highercount) / (highercount+lowercount+samecount)	
					likelisame=float (samecount) / (highercount+lowercount+samecount)	
					likelilow=float (lowercount) / (highercount+lowercount+samecount)	
					#print "carda:{} cardb:{} cardc:{} likelihood of higher:{} lower:{} same:{}".format(currcarda,currcardb,currcardc,likelihigh,likelilow,likelisame)
					cardremoves[currcarda][currcardb][currcardc] = likelihigh
		maxval = 0.0
		maxcards= []
		for acard in cardremoves:
			for bcard in cardremoves[acard]:
				for ccard in cardremoves[acard][bcard]:
					if maxval < cardremoves[acard][bcard][ccard]:
						maxval =cardremoves[acard][bcard][ccard]
						maxcards = [acard,bcard,ccard]	
					#print "acard:{} bcard:{} ccard:{} likelihood:{}".format(acard,bcard,ccard,cardremoves[acard][bcard][ccard])
		return (maxval, maxcards)
		#return likelihigh

	
	def chooseswap(self):
		#Q(s,a) == E[r(s,a)+ gamma (sum over possible states   P( possiblestate | s,a) V*(possiblestate)   )
		# V*(possiblestate) = E[sum over i    gamma^i r_(possstate +i)    ]
		# since we only have one action,  it's really just expected value-- how many
		# wins are possible for each swap
		# Q_n(s,a) <-- (1-alpha_n) Q_(n-1)(s,a) + alpha_n[r + gamma( max a' Q_(n-1)(s',a'))]
		# alpha_n = 1 / (1+visits to (s,a))
		# because it's nondeterministic
		currhandval = hands.handval(self.hand)[0]
		wins = self.learnedvals[currhandval][1]
		losses = self.learnedvals[currhandval][0]
		#print "learnedvals for current handval of {}... W:{} L:{}".format(currhandval,wins,losses  )
		likeli = float(wins + 1) / (wins + losses + 2)
		#print "\tlikelihood of winning with this hand:{}".format(likeli)
		losslikeli = float(losses + 1) / (wins + losses +2)
		#print "\t\tloss likelihood:{} \t sum:{}".format(losslikeli,likeli+losslikeli)
		#now calculate if we swap two cards. -- first get the higher val we can get with swapping
		# then the likelihood of any higher value
		#print "entering highervals1:"
		one= self.highervals1(list(self.hand))
		#print "entering highervals2:"
		two = self.highervals2(list(self.hand))
		#print "entering highervals3:"
		three = self.highervals3(list(self.hand))
		maxval = likeli
		ret = []
		if one[0] > maxval:
			maxval = one[0]
			ret= one[1]
		if two[0] > maxval:
			maxval = two[0]
			ret= two[1]
		if three[0] > maxval:
			maxval = three[0]
			ret= three[1]
		#return random.sample(self.hand, random.randint(0,3))
		return ret

	def recordwin(self, val):
		stat = ''
		if val == self.learnerid:
			stat = 'W'
		elif val == 'tie':
			print "I tied. T"
		else:
			stat = 'L'
		print stat
		outstring = "{}:{}:{} \n".format(" ".join(self.hand),hands.handval(self.hand),stat)
		with open(self.store, 'a') as s:
			s.write(outstring)
		pass
