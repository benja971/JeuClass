import pygame
from pygame.locals import *

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()



class Perso:
	def __init__(self):
		self.v = 6
		self.img = bank["perso"]
		self.rect = self.img.get_rect()
		self.rect.x = 102
		self.rect.y = 102


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
		self.v = 3
		self.rect = self.img.get_rect()
		self.rect.x = 500
		self.rect.y = 500
		
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
	"fond": pygame.image.load("bg2-bell.jpg").convert()
}

continuer = True
pygame.key.set_repeat(4, 4)

perso = Perso()

i = 0
enemyList = []

while continuer:
	horloge.tick(60)
	i += 1

	touches = pygame.key.get_pressed()
	events = pygame.event.get()

	perso.move(touches)

	for enemy in enemyList:
		enemy.move(perso)

	if touches[K_ESCAPE]:
		continuer = False
	

	if i%100 is 0:
		new = True
		for enemy in enemyList:
			if enemy.v < 5:
				enemy.v += 1
				new = False

		# si tous les ennemis ont une vitesse de 5 ou
		# s'il n'y en a pas alors on ajoue un ennemi
		if new:
			enemyList.append(Enemy())



	fenetre.blit(bank["fond"], (0, 0))
	fenetre.blit(bank["perso"], perso.rect)

	for enemy in enemyList:
		# print(enemyList, end = '\r')
		fenetre.blit(bank["mort"], enemy.rect)

	pygame.display.update()	