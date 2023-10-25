import pygame

# ----------------------------------------------------------------
# Módulo class Fondo.py 
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



