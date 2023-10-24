import pygame
import sys
import random
from settings import Settings
from classPieza import Pieza
from plantilla import Plantilla
from matrizFondo import MatrizFondo
from classFondo import Fondo

# ----------------------------------------------------------------
# Módulo Principal (main.py)
# 			
# ----------------------------------------------------------------
class Game:
	def __init__(self):
		pygame.init()

		self.settings = Settings()
		self.matrizFondo = MatrizFondo(self.settings.columnas, self.settings.filas)
		self.plantilla = Plantilla()
		self.pieza = None
		self.ultimo_update = pygame.time.get_ticks()

		self.pantalla = pygame.display.set_mode(self.settings.resolucion)
		self.reloj = pygame.time.Clock()

		self.instanciar_fondo()


	def instanciar_fondo(self):

		for i in range(self.settings.filas):
			for ii in range(self.settings.columnas):
				self.matrizFondo.matriz[i][ii] = Fondo(self, ii, i)



	def instanciar_pieza(self):

		if self.settings.otraPieza:
			self.settings.otraPieza = False
			x = self.settings.xInicial
			y = self.settings.yInicial
			piezas = self.settings.piezas
			color = self.settings.colorPiezas

			nro_rnd = random.randrange(len(piezas))
			elegida = piezas[nro_rnd]
			idPieza = self.plantilla.pieza[elegida]
			coloresPieza = color[nro_rnd]

			self.pieza = Pieza(self, x, y, idPieza, coloresPieza)
			#return self.pieza


	def update(self):
		pygame.display.set_caption(str(int(self.reloj.get_fps())))

		self.instanciar_pieza()

		pygame.display.flip()
		self.reloj.tick(self.settings.FPS) 


	def draw(self):
		self.pantalla.fill(self.settings.colorFondo2)

		for i in range(self.settings.filas):
			for ii in range(self.settings.columnas):
				self.matrizFondo.matriz[i][ii].dibuja()

		if self.pieza:
			self.pieza.dibuja()

		ancho = self.settings.columnas * self.settings.tileX + 1
		alto = self.settings.filas * self.settings.tileY + 1
		pygame.draw.rect(self.pantalla, (0, 0, 0), (0, 0, ancho, alto), 1)


	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif event.key == pygame.K_RETURN and self.settings.estado['menuPrincipal']:
					self.settings.estado.menuPrincipal = False
					self.settings.estado.enJuego = True
					#pygame.mixer.music.stop()

				elif event.key == pygame.K_LEFT and self.settings.estado['enJuego']:
					self.settings.controles['izquierda'] = True

				elif event.key == pygame.K_RIGHT and self.settings.estado['enJuego']:
					self.settings.controles['derecha'] = True

				elif event.key == pygame.K_SPACE and self.settings.estado['enJuego']:
					self.settings.controles['rotar'] = True

				elif event.key == pygame.K_z and self.settings.estado['enJuego']:
					calculo = pygame.time.get_ticks()
					if calculo - self.ultimo_update > 199:
						self.ultimo_update = calculo
						self.settings.otraPieza = True


		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_DOWN]:
			self.settings.controles['abajo'] = True



	def bucle_principal(self):
		while self.settings.estado['running']:
			self.check_event()
			self.update()
			self.draw()


if __name__ == '__main__':
	game = Game()
	game.bucle_principal()

