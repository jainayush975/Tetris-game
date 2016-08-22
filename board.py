from gameplay import *
from block import *


class Board(Gameplay,Block):

	def __init__(self):
		pass

	def checkgameover(self):
		self.checkRowEmpty()
		if not self.emptylist:
			return True
		else:
			print "EMPTYLIST =>",self.emptylist
			return False
	
	def delrow():
		i=len(self.fulllist)
		a=i
		b=i+1
		while b<len(self.gameboard[0]):
			if b not in self.fulllist:
				self.gameboard[a]=self.gameboard[b]
				b-=1
				a-=1
			else:
				b-=1
				i+=1
		self.gameboard[0]=self.emptyrow



