import pygame

# ----------------------------------------------------------------
# Módulo class Fondo.py 
# 			
# ----------------------------------------------------------------
class Fondo:
	def __init__(self, game, columna, fila):
		self.game = game 

		self.columna = columna
		self.fila = fila
		self.valor = 0


	def dibuja(self):

		colorFondo = self.game.settings.colorMarco
		colorRastro = self.game.settings.colorRastroPieza
		
		ancho = self.game.settings.tileX
		alto = self.game.settings.tileY

		x = self.columna * self.game.settings.tileX
		y = self.fila * self.game.settings.tileY
		#posMatriz = self.game.fondo[i][ii]

		if self.valor == 0:
			pygame.draw.rect(self.game.pantalla, colorFondo, (x, y, ancho, alto))
		else:
			pygame.draw.rect(self.game.pantalla, colorRastro, (x, y, ancho, alto))


	@staticmethod
	def check_lineDone(game):

		if not game.settings.checkeando_matriz:
			return

		filas = game.settings.filas

		for i in range(filas - 1, 0, -1):
			matrizLinea = game.matrizFondo.matriz[i]

			contador_cols = 0

			for cols in matrizLinea:
				if cols.valor != 0:
					contador_cols += 1

			if contador_cols == 14:
				game.settings.lineas += 1
				game.actualizar_matrizFondo(i)
				game.settings.checkeando_matriz = False

