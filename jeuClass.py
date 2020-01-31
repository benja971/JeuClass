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

font2 = pygame.font.Font('RioGrande.ttf', 55)

txtSingleplayer = font2.render("Singleplayer", 1, (255, 0, 0))
SingleplayerRect = Rect(450, 140, 365, 55)

txtMultiplayer = font2.render("Multiplayer", 1, (255, 0, 0))
MultiplayerRect = Rect(455, 255, 350, 55)

txtInfos = font2.render("Informations", 1, (255, 0, 0))
InfosRect = Rect(440, 365, 385, 35)

txtQuit = font2.render("Exit", 1, (255, 0, 0))
QuitRect = Rect(570, 460, 120, 40)

sonswitchmemu = pygame.mixer.Sound("1978.wav")


bank = {
	"perso": pygame.image.load("Dragon1.png").convert_alpha(),
	"mort": pygame.image.load("mort.png").convert_alpha(),
	"fondM": pygame.image.load("background.jpg").convert_alpha(),
	"fondJ": pygame.image.load("Fond d'écran .jpg").convert_alpha(),

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

continuer = True
state = 'menu'
i = 0
x = 0
y = 0

enemyList = []
enemyList.append(Enemy())

pygame.key.set_repeat(4, 4)

while continuer:
	horloge.tick(120)
	i += 1

	touches = pygame.key.get_pressed()
	events = pygame.event.get()


	if state == 'menu':
		fenetre.blit(bank["fondM"], (0, 0))
		select = Rect(x, y, 1, 1)

		if touches[K_ESCAPE]:
			continuer = False

		for event in pygame.event.get():
			if select.colliderect(SingleplayerRect):
				if event.type == MOUSEBUTTONDOWN:
					sonswitchmemu.play()
					state = 'Singleplayer'

			if select.colliderect(MultiplayerRect):
				if event.type == MOUSEBUTTONDOWN:
					sonswitchmemu.play()
					state = 'Multiplayer'

			if select.colliderect(InfosRect):
				if event.type == MOUSEBUTTONDOWN:
					sonswitchmemu.play()
					print("Infos.....")

			if select.colliderect(QuitRect):
				if event.type == MOUSEBUTTONDOWN:
					sonswitchmemu.play()
					continuer = False


			if event.type == MOUSEMOTION:
				x = event.pos[0]
				y = event.pos[1]

		if select.colliderect(SingleplayerRect):
			txtSingleplayer = font2.render("Singleplayer", 1, (255, 255, 255))
		else:
			txtSingleplayer = font2.render("Singleplayer", 1, (255, 0, 0))

		if select.colliderect(MultiplayerRect):
			txtMultiplayer = font2.render("Multiplayer", 1, (255, 255, 255))
		else:
			txtMultiplayer = font2.render("Multiplayer", 1, (255, 0, 0))

		if select.colliderect(InfosRect):
			txtInfos = font2.render("Informations", 1, (255, 255, 255))
		else:
			txtInfos = font2.render("Informations", 1, (255, 0, 0))

		if select.colliderect(QuitRect):
			txtQuit = font2.render("Exit", 1, (255, 255, 255))
		else:
			txtQuit = font2.render("Exit", 1, (255, 0, 0))

		fenetre.blit(txtSingleplayer, (450, 140))
		fenetre.blit(txtMultiplayer, (1262/2 - MultiplayerRect.w/2, 3*(632/8)+10))
		fenetre.blit(txtInfos, (1262/2 - InfosRect.w/2, 4*(632/8)+40))
		fenetre.blit(txtQuit, (1262/2 - QuitRect.w/2, 5*(632/8)+60))

	if state == 'Singleplayer':
		fenetre.blit(bank["fondJ"], (0, 0))
		
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
			fenetre.blit(bank["mort"], enemy.rect)

	pygame.display.flip()	