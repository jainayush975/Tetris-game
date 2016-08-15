import random
from gameplay import *
class Block(Gameplay):

	codinat = []

	def __init__(self):
		pass

	def draw(self):
		x=random.randint(0,3)
		
		if x==0:	#like  XXXX
			self.codinat = [[15,1],[16,1],[17,1],[18,1]]
		elif x==1:       
			self.codinat = [[18,2],[16,1],[17,1],[17,2]]
		elif x==2:       
			self.codinat = [[16,2],[16,1],[17,1],[17,2]]
		elif x==3:       
			self.codinat = [[15,1],[16,1],[17,1],[16,2]]
		elif x==4:       
			self.codinat = [[15,1],[16,1],[17,1],[17,2]]
		self.setvalues("X")
		return 

	def setvalues(self,val):
		self.gameboard[self.codinat[0][1]][self.codinat[0][0]]=val
		self.gameboard[self.codinat[1][1]][self.codinat[1][0]]=val
		self.gameboard[self.codinat[2][1]][self.codinat[2][0]]=val
		self.gameboard[self.codinat[3][1]][self.codinat[3][0]]=val
		return 

	def check(self,val):
		flag1=0
		flag2=0
		flag3=0
		flag4=0


		if self.gameboard[self.codinat[0][1]][self.codinat[0][0]+val] != " ":
			if not [self.codinat[0][0]+val,self.codinat[0][1]] in self.codinat:
				flag1 = 1;
		if self.gameboard[self.codinat[1][1]][self.codinat[1][0]+val] != " ":
			if not [self.codinat[1][0]+val,self.codinat[1][1]] in self.codinat:
				flag2 = 1;
		if self.gameboard[self.codinat[2][1]][self.codinat[2][0]+val] != " ":
			if not [self.codinat[2][0]+val,self.codinat[2][1]] in self.codinat:
				flag3 = 1;
		if self.gameboard[self.codinat[3][1]][self.codinat[3][0]+val] != " ":
			if not [self.codinat[3][0]+val,self.codinat[3][1]] in self.codinat:
				flag4 = 1;
		if flag1==1 or flag2==1 or flag3==1 or flag4==1:
			return 0
		else:
			return 1



	def movecodinat(self,val):
		self.codinat[0][0] += val
		self.codinat[1][0] += val
		self.codinat[2][0] += val
		self.codinat[3][0] += val
		return




	def moveleft(self):
		if self.check(-1)==1:
			self.setvalues(" ")
			self.movecodinat(-1)
			self.setvalues("X")
		return 



g1 = Gameplay()
b1 = Block()
b1.draw()
b1.printboard()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.printboard()

