from block import *
from board import *
clock = pygame.time.Clock()
colour = [
(255, 255, 255),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(0, 0, 0)
]
red = (225,0,0)

def displaygame(sx,sy):
	#global gamedisplay
	px = sx/32.0;py = sy/34.0
	for a in range(len(Block.gameboard)):
		for b in range(len(Block.gameboard[a])):
			if Block.gameboard[a][b]==1:
				pygame.draw.rect(gamedisplay,colour[8],[px*(b+1),py*(a+1),px,py])
			else:
				pygame.draw.rect(gamedisplay,colour[0],[px*(b+1),py*(a+1),px,py])
	pygame.draw.rect(gamedisplay,red,[0,0,px,sy])
	pygame.draw.rect(gamedisplay,red,[0,0,sx,py])
	pygame.draw.rect(gamedisplay,red,[sx-px,0,px,sy-py])
	pygame.draw.rect(gamedisplay,red,[0,sy-py,sx,py])
	pygame.display.update()
	clock.tick(8)

def playinggame():
	stone.qt = False
	stone.newblock()
	#events = pygame.event.get()
	changeleft=0;changeright=0
	while not stone.qt:
		displaygame(sizex,sizey)
		stone.movedown()
		#stone.qt = Board.checkgameover(b1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				stone.qt = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					changeleft = 1
				elif event.key == pygame.K_d:
					changeright = 1
				elif event.key == pygame.K_s:
					
					stone.rotate()
				elif event.key == pygame.K_SPACE:
					stone.directbottom()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					changeleft = 0
				if event.key == pygame.K_d:
					changeright = 0
		stone.moveleft(changeleft)
		stone.moveright(changeright)
		#print stone.printboard()
		#print b1.printboard()


g1 = Gameplay()
stone = Board()
b1 = Block()

sizex=640
sizey=600
pygame.init()
gamedisplay = pygame.display.set_mode((sizex,sizey))
gamedisplay.fill(colour[0])
pygame.display.update()	
playinggame()
print "Game Over"
gamedisplay.fill(colour[0])
pygame.display.update()	

