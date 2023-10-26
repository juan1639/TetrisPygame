import pygame

# ----------------------------------------------------------------
# Módulo classPieza.py
# 			
# ----------------------------------------------------------------
class Pieza:
	def __init__(self, game, x, y, idPieza, coloresPieza):

		self.game = game 

		self.x = x
		self.y = y 
		self.idPieza = idPieza
		self.coloresPieza = coloresPieza
		self.rotacion = 0



	def dibuja(self):
		self.actualiza()

		ancho = self.game.settings.tileX
		alto = self.game.settings.tileY

		rotacion_idPieza = self.averiguar_rotacion()

		for relPos in rotacion_idPieza:
			x = (self.x + relPos[0]) * ancho
			y = (self.y + relPos[1]) * alto

			pygame.draw.polygon(self.game.pantalla, self.coloresPieza[2], ((x, y), (x + ancho, y + ancho), (x, y + ancho)))
			pygame.draw.polygon(self.game.pantalla, self.coloresPieza[0], ((x, y), (x + ancho, y), (x + ancho, y + ancho)))



	def actualiza(self):

		if not self.game.settings.estado['enJuego']:
			return

		if self.game.settings.controles['izquierda']:

			self.x -= 1
			if self.check_colision():
				self.x += 1

			self.game.settings.controles['izquierda'] = False

		# ---------------------------------------------------
		elif self.game.settings.controles['derecha']:

			self.x += 1
			if self.check_colision():
				self.x -= 1

			self.game.settings.controles['derecha'] = False

		# ---------------------------------------------------
		elif self.game.settings.controles['abajo']:

			self.y += 1
			if self.check_colision():
				self.y -= 1

				if self.y <= 2:
					self.game.settings.estado['gameOver'] = True
					self.game.settings.estado['enJuego'] = False

				self.game.settings.otraPieza = True
				self.game.settings.checkeando_matriz = True
				self.dejar_rastro()

			self.game.settings.controles['abajo'] = False

		# ---------------------------------------------------
		elif self.game.settings.controles['rotar']:

			bck_rotacion = self.rotacion
			self.rotacion += 1
			if self.rotacion >= 4:
				self.rotacion = 0

			if self.check_colision():
				self.rotacion = bck_rotacion

			self.game.settings.controles['rotar'] = False


	def check_colision(self):

		rotacion_idPieza = self.averiguar_rotacion()

		for relPos in rotacion_idPieza:
			colX = self.x + relPos[0]
			colY = self.y + relPos[1]

			if colX > self.game.settings.columnas - 1 or colX < 0:
				return True

			if colY > self.game.settings.filas - 1:
				return True

			posMatriz = self.game.matrizFondo.matriz[colY][colX]
			if posMatriz.valor != 0:
				return True

		return False


	def averiguar_rotacion(self):

		parte_array = self.rotacion * 4
		rotacion_idPieza = []

		for i in range(len(self.idPieza)):
			if i == parte_array or i == parte_array + 1 or i == parte_array + 2 or i == parte_array + 3:
				rotacion_idPieza.append(self.idPieza[i])

		return rotacion_idPieza


	def dejar_rastro(self):

		rotacion_idPieza = self.averiguar_rotacion()

		for relPos in rotacion_idPieza:
			x = self.x + relPos[0]
			y = self.y + relPos[1]

			rastro = self.game.matrizFondo.matriz[y][x]
			rastro.valor = 9

