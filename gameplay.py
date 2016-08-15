

class Gameplay:
	gameboard = [[" "]*34 for i in range(32)]
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
	i=0
	fulllist = []
	emptylist = []
	score = 0

	def __int__(self):
		pass
        def checkRowFull(self):
		i=0
                for row in gameboard:
                        if row == fullrow:
				fulllist.append(i)
			i=i+1
		return fulllist



	def checkRowEmpty(self):
		i=0
		for row in gameboard:
			if row == emptyrow:
				emptylist.append(i)
			i=i+1
		return emptylist

	def printboard(self):
		for row in self.gameboard:
			for coloumn in row:
				print(coloumn),
			print

		#print()
		print("        Your Score :",self.score)#,print(self.score)
	
#g1=Gameplay()
#g1.printboard()
