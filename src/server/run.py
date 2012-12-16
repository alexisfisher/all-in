import poker,random

if __name__ == "__main__":
	print "ok. starting."
	deck = poker.poker()
	#print deck.deck
	deck.shuffle()
	player1 = 'b'
	deck.registerPlayer(player1)
	player2 = 'c'
	deck.registerPlayer(player2)
	hand1 = deck.deal(player1)
	hand2 = deck.deal(player2)
	print "hand1:{}".format(" ".join(hand1))
	print "hand2:{}".format(" ".join(hand2))
	select1 = random.randint(0,3)
	select2 = random.randint(0,3)
	hand1= deck.swap(player1,random.sample(hand1, select1))
	print "{} is swapping {} random cards.".format(player1, select1)
	print "\t{}".format(" ".join(hand1))
	#hand2= deck.swap(player2,hand2[:-select2])
	hand2= deck.swap(player2,random.sample(hand2, select2))
	#hand2= deck.swap(player2,[hand2.pop(), hand2.pop()])
	print "{} is swapping {} random cards.".format(player2, select2)
	print "\t{}".format(" ".join(hand2))
	
	deck.resolve()

	#print deck.deck
