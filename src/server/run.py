import poker

if __name__ == "__main__":
	print "ok. starting."
	deck = poker.poker()
	print deck.deck
	deck.shuffle()
	player1 = 'b'
	deck.registerPlayer(player1)
	player2 = 'c'
	deck.registerPlayer(player2)
	hand1 = deck.deal(player1)
	hand2 = deck.deal(player2)
	print "hand1:{}".format(" ".join(hand1))
	print "hand2:{}".format(" ".join(hand2))
	print "swapping last two cards."
	hand1= deck.swap(player1,[hand1.pop(), hand1.pop()])
	hand2= deck.swap(player2,[hand2.pop(), hand2.pop()])
	print "hand1:{}".format(" ".join(hand1))
	print "hand2:{}".format(" ".join(hand2))
	
	deck.resolve()
	print deck.deck
