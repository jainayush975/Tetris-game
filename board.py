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

	def rotatecheck(self,identity):
		co = []
		c1 = self.shapes[self.shape][identity]
		for i in range(len(c1)):
			co.append([c1[i][0]+self.offsetx,c1[i][1]+self.offsety])
		for row in co:
			if row[0]<=1 or row[0]>=34 or row[1]>=30:
				return 0
		for row in co:
			if self.gameboard[row[1]][row[0]]==1:
				if not [row[0],row[1]] in self.codinat:
					return 0
		return 1

	def makecodinat(self):
		self.codinat = []
		c1 = self.shapes[self.shape][self.shapeid]
		print self.shape,self.shapid
		for i in range(len(c1)):
			self.codinat.append([c1[i][0]+self.offsetx,c1[i][1]+self.offsety])
		return 


	def rotate(self):
		
		print "Before:",self.codinat
		if self.rotatecheck((self.shapeid+1)%4):
			self.shapeid = ((self.shapeid+1)%4)
			self.makecodinat()
			print self.codinat

		return 
				



