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

class learner:
	hand = []
	learnerid = 'learner'	
	def __init__(self,inhand):
		print "in learner init"
		self.hand = self.sorthand(inhand)

#['H14','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S14','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','D14','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','C14','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13' ]
	def sorthand(self,hand):
		#TODO
		return hand

	def chooseswap(self):
		#TODO choose
		return random.sample(self.hand, random.randint(0,3))
	
