import pygame
import random

# ----------------------------------------------------------------
# Módulo class Marcadores.py 
# 			
# ----------------------------------------------------------------
class Marcadores(pygame.sprite.Sprite):
	def __init__(self, game, x, y, size, texto, color):
		super().__init__()

		self.game = game

		self.x = x
		self.y = y

		self.texto = texto
		self.color = color

		self.font = pygame.font.SysFont('impact', size)
		self.image = self.font.render(self.texto, True, self.color)
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
	


	def update(self):
		txtMarcador = ''

		if self.texto == 'Lineas: ':
			txtMarcador = self.texto + str(self.game.settings.lineas)
		elif self.texto == 'Record: ':
			txtMarcador = self.texto + str(self.game.settings.record)
		elif self.texto == 'Nivel: ':
			txtMarcador = self.texto + str(self.game.settings.nivel)

		self.image = self.font.render(txtMarcador, True, self.color)


class infoLineas(pygame.sprite.Sprite):
	def __init__(self, game, cuantas):
		super().__init__()
		self.game = game 

		self.x = int(self.game.settings.resolucion[0] / 4)
		self.y = int(self.game.settings.resolucion[1] / 3.5)
		self.cuantas = str(cuantas)
		self.size = 60
		self.color = (240, 240, 240)

		self.font = pygame.font.SysFont('impact', self.size)
		self.image = self.font.render('+ ' + self.cuantas, True, self.color)
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x, self.y)

		self.ultimo_update = pygame.time.get_ticks()


	def update(self):
		self.color = (255, random.randrange(200) + 55, 0)
		self.image = self.font.render('+ ' + self.cuantas, True, self.color)

		calculo = pygame.time.get_ticks()
		if calculo - self.ultimo_update > self.game.settings.tiempo_infoLineas:
			self.kill()


