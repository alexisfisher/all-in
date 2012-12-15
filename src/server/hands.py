
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
	if f == '0':
		return '00'
	else: 
		if s:
			return f+str(s)

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
	subcards = [x for x in cards if cardval(x) == three]
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
	#returns 0 or high card
	hcard = 0
	cardvals = []
	for card in cards:
		cardvals.append(cardval(card))
	cardvals = sorted(cardvals)
	curr = cardvals[0]
	for val in cardvals[:1]:
		if val == curr + 1:
			curr = val
	if curr == highcard(cards):
		hcard = curr
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
