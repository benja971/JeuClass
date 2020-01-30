import pygame, random, os
from pygame.locals import *

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

os.system('cls')

class Perso:
	def __init__(self):
		self.v = 6
		self.img = bank["perso"]
		self.rect = self.img.get_rect()
		self.rect.x = 102
		self.rect.y = 102
		self.vies = 10


	def move(self, touches):
		if touches[K_LEFT] and self.rect.x - self.rect.w > -self.rect.w:
			self.rect.x -= self.v

		if touches[K_RIGHT] and self.rect.x + self.rect.w  < 1262:
			self.rect.x += self.v	

		if touches[K_UP] and self.rect.y - self.rect.h > -self.rect.h:
			self.rect.y -= self.v

		if touches[K_DOWN] and self.rect.y + self.rect.h < 632:
			self.rect.y += self.v	



class Enemy:
	def __init__(self):
		self.img = bank["mort"]
		self.v = 1
		self.rect = self.img.get_rect()
		self.rect.x = random.randint(200, 1062)
		self.rect.y = random.randint(100, 532)
		
	def collisions(self, perso):

		return self.rect.colliderect(perso.rect)


	def move(self, perso):
		if perso.rect.x < self.rect.x:
			self.rect.x -= self.v

		if perso.rect.x > self.rect.x:
			self.rect.x += self.v

		if perso.rect.y < self.rect.y:
			self.rect.y -= self.v

		if perso.rect.y > self.rect.y:
			self.rect.y += self.v



fenetre = pygame.display.set_mode((1262, 632))
horloge = pygame.time.Clock()

bank = {
	"perso": pygame.image.load("Dragon1.png").convert_alpha(),
	"mort": pygame.image.load("mort.png").convert_alpha(),
	"fond": pygame.image.load("Fond d'écran .jpg").convert_alpha(),

	"vie100": pygame.image.load("vie100.png").convert_alpha(),
	"vie90": pygame.image.load("vie90.png").convert_alpha(),
	"vie80": pygame.image.load("vie80.png").convert_alpha(),
	"vie70": pygame.image.load("vie70.png").convert_alpha(),
	"vie60": pygame.image.load("vie60.png").convert_alpha(),
	"vie50": pygame.image.load("vie50.png").convert_alpha(),
	"vie40": pygame.image.load("vie40.png").convert_alpha(),
	"vie30": pygame.image.load("vie30.png").convert_alpha(),
	"vie20": pygame.image.load("vie20.png").convert_alpha(),
	"vie10": pygame.image.load("vie10.png").convert_alpha(),
}

perso = Perso()
enemy = Enemy()

font2 = pygame.font.Font('RioGrande.ttf', 55)

txtSingleplayer = font2.render("Singleplayer", 1, (255, 0, 0))
SingleplayerRect = Rect(1262/2 - SingleplayerRect.w/2, 2*(632/8)-20))
print(*SingleplayerRect)

txtMultiplayer = font2.render("Multiplayer", 1, (255, 0, 0))
MultiplayerRect = txtMultiplayer.get_rect()

txtInfos = font2.render("Informations", 1, (255, 0, 0))
InfosRect = txtInfos.get_rect()

txtQuit = font2.render("Exit", 1, (255, 0, 0))
QuitRect = txtQuit.get_rect()

test = bank["perso"].get_rect()


continuer = True
state = 'menu'
i = 0
enemyList = []

enemyList.append(Enemy())

pygame.key.set_repeat(4, 4)

while continuer:
	horloge.tick(120)
	i += 1

	touches = pygame.key.get_pressed()
	events = pygame.event.get()

	fenetre.blit(bank["fond"], (0, 0))

	if state == 'menu':

		if touches[K_ESCAPE]:
			continuer = False

		if test.colliderect(SingleplayerRect):
			print("touche")

		for event in pygame.event.get():
			if event.type == MOUSEMOTION:
				test.x = event.pos[0]
				test.y = event.pos[1]

		fenetre.blit(txtSingleplayer, (1262/2 - SingleplayerRect.w/2, 2*(632/8)-20))
		fenetre.blit(txtMultiplayer, (1262/2 - MultiplayerRect.w/2, 3*(632/8)+10))
		fenetre.blit(txtInfos, (1262/2 - InfosRect.w/2, 4*(632/8)+40))
		fenetre.blit(txtQuit, (1262/2 - QuitRect.w/2, 5*(632/8)+60))
		fenetre.blit(bank["perso"], (test.x - test.w, test.y))


	if state == 'Singleplayer':
		
		perso.move(touches)
		enemy.collisions(perso)

		for enemy in enemyList:
			enemy.move(perso)

		if touches[K_ESCAPE]:
			continuer = False
		

		if i%1000 is 0:
			new = True
			for enemy in enemyList:
				if enemy.v < 4:
					enemy.v += 1
					new = False

			# si tous les ennemis ont une vitesse de 5 ou
			# s'il n'y en a pas alors on ajoue un ennemi
			if new:
				enemyList.append(Enemy())

		for enemy in enemyList:
			if enemy.rect.colliderect(perso.rect):
				perso.vies -= 1
				perso.rect.x = random.randint(200, 1062)
				perso.rect.y = random.randint(100, 532)


		fenetre.blit(bank["perso"], perso.rect)

		if perso.vies == 10:
			fenetre.blit(bank["vie100"], (10,10))

		if perso.vies == 9:
			fenetre.blit(bank["vie90"], (10,10))

		if perso.vies == 8:
			fenetre.blit(bank["vie80"], (10,10))

		if perso.vies == 7:
			fenetre.blit(bank["vie70"], (10,10))

		if perso.vies == 6:
			fenetre.blit(bank["vie60"], (10,10))

		if perso.vies == 5:
			fenetre.blit(bank["vie50"], (10,10))

		if perso.vies == 4:
			fenetre.blit(bank["vie40"], (10,10))

		if perso.vies == 3:
			fenetre.blit(bank["vie30"], (10,10))
		
		if perso.vies == 2:
			fenetre.blit(bank["vie20"], (10,10))

		if perso.vies == 1:
			fenetre.blit(bank["vie10"], (10,10))

		if perso.vies == 0:
			state = 'menu'

		for enemy in enemyList:
			# print(enemyList, end = '\r')
			fenetre.blit(bank["mort"], enemy.rect)

	pygame.display.flip()	