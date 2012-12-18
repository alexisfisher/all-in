
def isroyalflush(cards):
	#check if cards are straight flush & high card is ace
	#returns highcard (ace) OR '00'
	highcard = isstraightflush(cards)
	if cardval(highcard) == 14:
		return highcard
	else:
		return '00'
		
def isstraightflush(cards):
	#isflush & isstraight
	#return high card or '00'
	f = isflush(cards)
	s = isstraight(cards)
	#print"f:{} s:{}".format(f,s)
	if f == '0':
		return '00'
	else: 
		if s:
			return f+str(s)
		else:
			return '00'

def isfourofakind(cards):
	#four of the cards are the same val
	cardvals = []
	pairval = 0
	for card in cards:
		cardvals.append(cardval(card))
	pairval = ispair(cards)
	if cardvals.count(pairval) < 4:
		pairval = 0
	return pairval
	pass
def isfullhouse(cards):
	# should be isthreeofakind & ispair
	# return val of threeofakind
	three= isthreeofakind(cards)
	subcards = [x for x in cards if cardval(x) != three]
	if len(subcards):
		if ispair(subcards):
			return three
		else:
			return 0

def isflush(cards):
	#same suit
	#return '0' if not same, HSDC if flush
	cardsuit = [x[0] for x in cards]
	#print "in isflush. cards:{} cardsuit:{} len(cards): {} cardsuit.count(cardsuit[0]): {}".format(" ".join(cards)," ".join(cardsuit), len(cards),cardsuit.count(cardsuit[0]))
	if len(cards) == cardsuit.count(cardsuit[0]):
		#print "\t lencards == count[0]"
		return cardsuit[0]
	else:
		return '0'

def isstraight(cards):
	#in order
	# returns 0 or high card
	#print cards
	hcard = 0
	cardvals = []
	for card in cards:
		cardvals.append(cardval(card))
	cardvals = sorted(list(set(cardvals)))
	if len(cardvals) == len(cards):
		#print "cardvals:{}".format(cardvals)
		curr = cardvals[0]
		for val in cardvals[1:]:
			if val == curr + 1:
				curr = val
		if curr == cardval(highcard(cards)):
			hcard = curr
		#now we check if cardval(highcard(cards)) == 14. if so, and if hcard == 0,
		if hcard == 0:
			#print "not a straight, checking if acey"
			if cardval(highcard(cards)) == 14:
				#print "we have an ace. cards[:4]:{}".format(cards[:4])
				subcards = [x for x in cards if cardval(x) != 14]
				#now we check to see if cardvals[:4] is a straight w/a high val of 4
				if (len(subcards) == 4) and (isstraight(subcards) == 5): 
					hcard = 5
	return hcard
		
def isthreeofakind(cards):
	#three are same val
	cardvals = []
	pairval = 0
	for card in cards:
		cardvals.append(cardval(card))
	pairval = ispair(cards)
	if cardvals.count(pairval) < 3:
		pairval = 0
	return pairval

def istwopair(cards):
	# two distinct ispairs
	# if < 2 pairs, return 0, else return val of high pair
	cardvals = []
	pairval1 = pairval2 = 0
	for card in cards:
		cardvals.append(cardval(card))
	pairval1 = ispair(cards)
	#now remove cards with cardval pairval1
	if pairval1:
		subcards = [x for x in cards if cardval(x) != pairval1 ]
		pairval2 = ispair(subcards)
	if pairval2:
		return max(pairval1, pairval2)
	else:
		return 0

def ispair(cards):
	#two of same val
	cardvals = []
	pairval = 0
	for card in cards:
		cardvals.append(cardval(card))
	for cval in cardvals:
		if cardvals.count(cval) > 1:
			pairval = cval
	return pairval

def highcard(cards):
	#return the highest card
	# if there's a pair, ok
	highestval = 0
	highest = ''
	for card in cards:
		cval= cardval(card)
		if int(cval) > highestval:
			highestval = cval
			highest = card
	return highest

def cardval(card):
	val = int(card.lstrip('HSDC'))
	#print "in cardval, card: {} val: {}".format(card,val)
	return val 

def handval(cards):
	#playerval = 0
	playerval = (0, highcard(cards))
	if ispair(cards):
		playerval = (1, ispair(cards))
	if istwopair(cards):
		playerval = (2, istwopair(cards))
	if isthreeofakind(cards):
		playerval = (3, isthreeofakind(cards))
	if isstraight(cards):
		playerval = (4, isstraight(cards))
	if isflush(cards) != '0':
		playerval = (5, isflush(cards))
	if isfullhouse(cards):
		playerval = (6, isfullhouse(cards))
	if isfourofakind(cards):
		playerval = (7, isfourofakind(cards))
	if isstraightflush(cards) != '00':
		playerval = (8, isstraightflush(cards))
	if isroyalflush(cards) != '00':
		playerval = (9, isroyalflush(cards))

	return playerval
