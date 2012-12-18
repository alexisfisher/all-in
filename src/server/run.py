import poker,random,learner

if __name__ == "__main__":
	deck = poker.poker()
	deck.shuffle()
	player1 = 'b'
	deck.registerPlayer(player1)
	player2 = 'learnerc'
	deck.registerPlayer(player2)
	hand1 = deck.deal(player1)
	hand2 = deck.deal(player2)
	l = learner.learner(hand2)
	l.learnerid = player2
	print "{}: {}".format(player1," ".join(hand1))
	print "{}: {}".format(player2," ".join(hand2))
	select1 = random.randint(0,3)
	hand1= deck.swap(player1,random.sample(hand1, select1))
	print "{} is swapping {} random cards.".format(player1, select1)
	print "\t{}".format(" ".join(hand1))
	hand2 = deck.swap(player2, l.chooseswap())	
	print "{} is swapping {} cards.".format(player2, len(hand2))
	print "\t{}".format(" ".join(hand2))

	#print "{}: {}".format(player1," ".join(hand1))
	#print "{}: {}".format(player2," ".join(hand2))
	winner = deck.resolve()
	print "Winner: {}".format(winner)
	l.recordwin(winner)
	#print deck.deck
