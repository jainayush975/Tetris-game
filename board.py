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
			return False
	
	def delrow(self):
		#print "in del row"
		#print self.fulllist
		#print "EMpty Row",self.emptyrow
		self.checkRowFull()
		#print "EMpty Row",self.emptyrow
		i=len(self.fulllist)
		#print "EMpty Row",self.emptyrow
		if i:
			self.updatescore(50)
			self.updatelevel()
			#print self.fulllist
			#print"Deleting Row"
			#print "EMpty Row",self.emptyrow
			a=self.fulllist[i-1]
			b=a-1
			while b>0:
				if b not in self.fulllist:
					self.gameboard[a]=self.gameboard[b]
					b-=1
					a-=1
				else:
					b-=1
			while a>=0:	
				print "EMpty Row",self.emptyrow,"changing"
				self.gameboard[a]=[0 for i in range(36)]
				a-=1

				



