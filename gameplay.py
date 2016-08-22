import pygame

class Gameplay:
	gameboard = [[0 for j in range(36)] for i in range(32)]
	fullrow = [0,0]
	fullrow.extend( [1] for i in range(32))
	fullrow.extend([0,0])
	emptyrow = [0 for i in range(36)]
	i=0 
	fulllist = []
	emptylist = []
	score = 0

	def __int__(self):
		pass
        def checkRowFull(self):
		self.fulllist = []
		i=0
		for row in self.gameboard[0:30]:
                        if row == self.fullrow:
				self.fulllist.append(i)
			i=i+1
		return self.fulllist



	def checkRowEmpty(self):
		self.emptylist = []
		i=0
		for row in self.gameboard[0:30]:
			if row == self.emptyrow:
				self.emptylist.append(i)
			i=i+1
		return self.emptylist

	def printboard(self):
		for row in self.gameboard:
			#for coloumn in row:
				#print(coloumn),
			print row

		#print()
		#print("        Your Score :",self.score)#,print(self.score)

#g1=Gameplay()
#g1.printboard()
'''
	for i in range(33):
		gameboard[0][i]="-"
		gameboard[31][i]="-"
	for i in range(31):
		gameboard[i][0]="|"
		gameboard[i][33]="|"
	gameboard[0][0]="+"
	gameboard[0][33]="+"
	gameboard[31][0]="+"
	gameboard[31][33]="+"

	fullrow = ["X" for i in range(34)]
	fullrow[0] = "|"
	fullrow[33] = "|"
	emptyrow = [" " for i in range(34)]
	emptyrow[0] = "|"
	emptyrow[33] = "|"
	'''
