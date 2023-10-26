import pygame

# ----------------------------------------------------------------
# Módulo class GameOver.py 
# 			
# ----------------------------------------------------------------
class gameOver(pygame.sprite.Sprite):
	def __init__(self, game, x, y, texto, size):
		super().__init__()
		self.game = game 

		self.x = x
		self.y = y

		self.texto = texto
		self.color = (240, 240, 240)
		self.size = size

		self.font = pygame.font.SysFont('impact', self.size)
		self.image = self.font.render(self.texto, True, self.color)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)


	def update(self):
		pass 


