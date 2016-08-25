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
(0, 0, 0),
(32,32,32),
(128,128,128)
]

fps = 9


def displaygame(sx,sy):
	gamedisplay.fill(colour[0])
	px = sx/36;py = sy/32
	for a in range(len(Block.gameboard[0:30])):
		for b in range(len(Block.gameboard[a])):
			if Block.gameboard[a][b]==1:
				pygame.draw.rect(gamedisplay,colour[10],[px*(b)+1,py*(a)+1,px-2,py-2])
			else:
				pygame.draw.rect(gamedisplay,colour[0],[px*(b),py*(a),px,py])
	
	
	pygame.draw.rect(gamedisplay,colour[9],[px*2-2,py*2-2,2,sy-4*py])
	pygame.draw.rect(gamedisplay,colour[9],[px*2-2,py*2-2,sx-4*px,2])
	pygame.draw.rect(gamedisplay,colour[9],[sx-2*px,py*2-2,2,sy-4*py])
	pygame.draw.rect(gamedisplay,colour[9],[py*2-2,sy-py-py,sx-4*px,2])
	
	scor = stone.givescore()
	lvl = stone.givelevel()
	print scor,lvl
	myfont = pygame.font.SysFont("bold",20)
	label = myfont.render("Your Score: "+str(scor), 1, colour[8])
	label1 = myfont.render("LEVEL: "+str(lvl), 1, colour[8])
	textrect=label.get_rect()
	textrect1=label1.get_rect()
	textrect.center = (sx+50,sy/2-20)
	textrect1.center = (sx+50,sy/2+20)
	gamedisplay.blit(label, textrect)
	gamedisplay.blit(label1, textrect1)
	pygame.display.update()
	clock.tick(fps-lvl)

def playinggame():
	stone.qt = False
	stone.newblock()
	changeleft=0;changeright=0
	while not stone.qt:
		displaygame(sizex,sizey)
		stone.movedown()
		stone.qt = Board.checkgameover(b1)
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
		Board.delrow(b1)


g1 = Gameplay()
b1 = Board()
stone = Block()

sizex=540
sizey=480
pygame.init()
gamedisplay = pygame.display.set_mode((sizex+200,sizey))
gamedisplay.fill(colour[0])
pygame.display.update()	
playinggame()
print "Game Over"
gamedisplay.fill(colour[0])
pygame.display.update()	

