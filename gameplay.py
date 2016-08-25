import pygame

class Gameplay:
	__score = 0
	gameboard = [[0 for j in range(36)] for i in range(32)]
	fullrow = [0,0]
	fullrow.extend( 1 for i in range(32))
	fullrow.extend([0,0])
	emptyrow = [0 for i in range(36)]
	i=0 
	fulllist = []
	emptylist = []
	LEVEL = 1
	sc =0 

	def __int__(self):
		pass
        def checkRowFull(self):
		self.fulllist = []
		i=0
		for row in self.gameboard[0:30]:
                        if row == self.fullrow:
				#print "fullrow",row ; print "Fullrow", self.fullrow
				self.fulllist.append(i)
			i=i+1
		return 



	def checkRowEmpty(self):
		self.emptylist = []
		i=0
		for row in self.gameboard[0:30]:
			if row == self.emptyrow:
				self.emptylist.append(i)
			i=i+1
		return

	def printboard(self):
		for row in self.gameboard:
			print row

	def updatescore(self,t):
		self.__score = self.__score + t
		sc = self.__score
		print "Score Updated", self.__score
		return 

	def updatelevel(self):
		self.LEVEL = int(self.__score/500)+1
		print "Level Updated"
		a = self.LEVEL
		return 


	def givelevel(self):
		a = self.LEVEL
		return a

	def givescore(self):
		a = self.__score
		print "returnnig=",self.__score
		return self.__score


