

class Gameplay:
	gameboard = [[" "]*34 for i in range(32)]
	fullrow = ["X" for i in range(34)]
	fullrow[0] = "|"
	fullrow[33] = "|"
	emptyrow = [" " for i in range(34)]
	emptyrow[0] = "|"
	emptyrow[33] = "|"
	i=0
	fulllist = []
	emptylist = []

        def __int__(self):

        def checkRowFull():
		i=0
                for row in gameboard:
                        if row == fullrow:
				fulllist.append(i)
			i++;
		return fulllist



	def checkRowEmpty():
		i=0
		for row in gameboard:
			if row == emptyrow:
				emptylist.append(i)
			i++;
		return emptylist


