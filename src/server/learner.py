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

class learner:
	hand = []
	learnerid = 'learner'	
	def __init__(self,inhand):
		self.hand = sorthand(inhand)


	def sorthand(hand):
		#TODO
		return hand

	
