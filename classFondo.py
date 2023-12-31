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

		lineas_alavez = 0
		filas = game.settings.filas

		for i in range(filas - 1, 0, -1):
			matrizLinea = game.matrizFondo.matriz[i]
			
			hasta_cuatro = True

			while (hasta_cuatro):
				contador_cols = 0

				for cols in matrizLinea:
					if cols.valor != 0:
						contador_cols += 1

				if contador_cols == 14:
					game.settings.lineas += 1
					lineas_alavez += 1
					game.settings.nivel = int(game.settings.lineas / 7) + 1
					game.settings.sonido['linea'].play()
					game.settings.sonido['linea'].set_volume(0.6)

					if game.settings.gravedad > 100:
						game.settings.gravedad -= game.settings.incremento_dificultad
						print(game.settings.gravedad)

					game.actualizar_matrizFondo(i)

				else:
					hasta_cuatro = False
					break

		game.instancia_infoLineas(lineas_alavez)
		game.settings.checkeando_matriz = False

