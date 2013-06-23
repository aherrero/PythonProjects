"""
Name        : 	game.py
Author      : 	Alex
Des			:	Juego de testing para la PyGame
"""

import sys, pygame
from pygame.locals import *
import random

width=640
height=480

class GameObject:
	"""Clase que implementa los metodos de objetos del juego, jugadores y enemigos"""
	def __init__(self, image, posx, posy):
		self.image = image
		self.pos = [posx,posy]
		self.dimension = image.get_rect() #devuelve rectangulo con dimensiones
		
	def move(self,posx,posy):
		self.pos[0] = self.pos[0]+posx
		self.pos[1] = self.pos[1]+posy	
		#limites
		if self.pos[0] <0 :
			self.pos[0]=0
		elif self.pos[0] >width -self.dimension.right :
			self.pos[0]=width -self.dimension.right
		elif self.pos[1] <0:
			self.pos[1]=0
		if self.pos[1] > height-self.dimension.bottom:
			self.pos[1]=height-self.dimension.bottom
			
	def setPos(self,posx,posy):
		self.pos[0] = posx
		self.pos[1] = posy	
		

def colision(player,mons):
	"""
	Colision entre dos objetos rectangulares de la clase GameObject.
	Devuelve True si hay colsion, False si no
	"""
	choque=False;
	esquina1=[player.pos[0],player.pos[1]];
	esquina2=[player.pos[0]+player.dimension.right,player.pos[1]];
	esquina3=[player.pos[0]+player.dimension.right,player.pos[1]+player.dimension.bottom];
	esquina4=[player.pos[0],player.pos[1]+player.dimension.bottom];
	
	if ((esquina1[0]>mons.pos[0] and esquina1[0]< (mons.pos[0]+ mons.dimension.right)) and (esquina1[1]>mons.pos[1] and esquina1[1]< (mons.pos[1]+ mons.dimension.bottom))):
		choque=True
	elif ((esquina2[0]>mons.pos[0] and esquina2[0]< (mons.pos[0]+ mons.dimension.right)) and (esquina2[1]>mons.pos[1] and esquina2[1]< (mons.pos[1]+ mons.dimension.bottom))):
		choque=True
	elif ((esquina3[0]>mons.pos[0] and esquina3[0]< (mons.pos[0]+ mons.dimension.right)) and (esquina3[1]>mons.pos[1] and esquina3[1]< (mons.pos[1]+ mons.dimension.bottom))):
		choque=True
	elif ((esquina4[0]>mons.pos[0] and esquina4[0]< (mons.pos[0]+ mons.dimension.right)) and (esquina4[1]>mons.pos[1] and esquina4[1]< (mons.pos[1]+ mons.dimension.bottom))):
		choque=True
	else:
		choque=False
	
	return choque

def meta(player):
	meta=False
	esquina3=[player.pos[0]+player.dimension.right,player.pos[1]+player.dimension.bottom];
	if esquina3[0] == width and esquina3[1] == height:
		meta=True
	
	return meta
	
		
def loadmusic(dirmusic):
	pygame.mixer.music.load(dirmusic)
	#pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)
	#pygame.mixer.music.stop()
	

def main():

	pygame.init()
	
	loadmusic('welcome.mid')

	#tamanio inicial pantalla
	screen = pygame.display.set_mode((width, height))

	#carga imagenes
	background = pygame.image.load('back.jpg').convert()
	monsterimage = pygame.image.load('monster.jpg').convert()
	playerimage = pygame.image.load('playerimage.jpg').convert()
	lost = pygame.image.load('lost.jpg').convert()
	win = pygame.image.load('win.jpg').convert()

	#crea objetos
	player = GameObject(playerimage, 0, 0)
	listmonster = []

	for x in range(6): 		#create 10 objects
		posxini=random.randint(80, width-80)	#80 o lo que mida el monster
		posyini=random.randint(80, height-80)
		o = GameObject(monsterimage,posxini ,posyini )	
		listmonster.append(o)

	#muestra en pantalla objetos
	screen.blit(background, (0, 0))
	screen.blit(player.image, player.pos)
	for o in listmonster:
		screen.blit(o.image, o.pos)
	pygame.display.update()

	"""
	K_UP                  up arrow
	K_DOWN                down arrow
	K_RIGHT               right arrow
	K_LEFT                left arrow
	"""
	
	reinicia=True
	speedmonster=[-2,2]

	#inicio juego
	while 1:
		#pulsacion de tecla para movimiento de jugador
		for event in pygame.event.get():
		  if event.type == KEYDOWN:
			#tecla pulsada
			speed=30
			if (event.key == K_ESCAPE):
				sys.exit()
			elif (event.key == K_UP or event.key == K_w):
				player.move(0,-speed)
			elif (event.key == K_DOWN or event.key == K_s):
				player.move(0,+speed)
			elif (event.key == K_RIGHT or event.key == K_a):
				player.move(speed,0)
			elif (event.key == K_LEFT or event.key == K_d):
				player.move(-speed,0)
			elif event.key == K_F1:
				if reinicia==False or meta(player):
					reinicia=True
					choque=False
					player.setPos(0,0)
					speedmonster[0]=speedmonster[0]-1
					speedmonster[1]=speedmonster[1]+1
					for o in listmonster:
						posxini=random.randint(80, width-80)
						posyini=random.randint(80, height-80)
						o.setPos(posxini,posyini)

				
		for o in listmonster:
			o.move(random.randint(speedmonster[0], speedmonster[1]),random.randint(speedmonster[0], speedmonster[1]))
			
		#actuacion
		choque=False
		for o in listmonster:
			choque=choque or colision(player,o)
			
		if choque:
			screen.blit(lost,( 0, 0))
			speedmonster=[-1,1]
			reinicia=False
		
		if not choque and reinicia:
			#muestra en pantalla
			screen.blit(background,( 0, 0))
			screen.blit(player.image, player.pos)
			for o in listmonster:
				screen.blit(o.image, o.pos)
		
		if meta(player):
			screen.blit(win,( 0, 0))

		#actualiza
		pygame.display.update()
		pygame.time.delay(10)
	
	
if __name__ == "__main__":
	main()
