import pygame

# ----------------------------------------------------------------
# Módulo class NextPieza.py 
# 			
# ----------------------------------------------------------------
class nextPieza:
	def __init__(self, game, x, y, idPieza, coloresPieza):
		self.game = game 

		self.x = x 
		self.y = y 
		self.idPieza = idPieza
		self.coloresPieza = coloresPieza
	


	@staticmethod
	def dibuja(game, nextPieza):

		ancho = game.settings.tileX
		alto = game.settings.tileY

		firstRot = nextPieza.idPieza[0:4]

		for relPos in firstRot:
			x = (nextPieza.x + relPos[0]) * ancho
			y = (nextPieza.y + relPos[1]) * alto

			pygame.draw.polygon(game.pantalla, nextPieza.coloresPieza[2], ((x, y), (x + ancho, y + ancho), (x, y + ancho)))
			pygame.draw.polygon(game.pantalla, nextPieza.coloresPieza[0], ((x, y), (x + ancho, y), (x + ancho, y + ancho)))

