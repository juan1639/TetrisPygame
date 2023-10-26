import pygame
import sys
import random
from settings import Settings
from classPieza import Pieza
from plantilla import Plantilla
from matrizFondo import MatrizFondo
from classFondo import Fondo
from classMarcadores import *
from classNextpieza import nextPieza
from classGameover import *

# ----------------------------------------------------------------
# Módulo Principal (main.py)
# 			
# ----------------------------------------------------------------
class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()

		self.settings = Settings()
		self.matrizFondo = MatrizFondo(self.settings.columnas, self.settings.filas)
		self.plantilla = Plantilla()
		self.pieza = None
		self.ultimo_update = pygame.time.get_ticks()

		self.pantalla = pygame.display.set_mode(self.settings.resolucion)
		self.reloj = pygame.time.Clock()

		self.lista_textos = pygame.sprite.Group()

		self.settings.sonido['musica'].load("./sonidos/assets_music.ogg")
		self.settings.sonido['musica'].play(loops=-1)
		self.settings.sonido['musica'].set_volume(0.6)

		self.instanciar_fondo()
		self.instanciar_marcadores()

		self.presentacion = gameOver(self, int((self.settings.resolucion[0] / 2) / 2), self.settings.resolucion[1] / 2, 'Game Over', 70)
		self.pulsaComenzar = gameOver(self, int((self.settings.resolucion[0] / 2) / 2), self.settings.resolucion[1] / 1.1, 'Pulse una tecla para jugar...', 28)
		self.lista_textos.add(self.presentacion, self.pulsaComenzar)



	def instanciar_fondo(self):

		for i in range(self.settings.filas):
			for ii in range(self.settings.columnas):
				self.matrizFondo.matriz[i][ii] = Fondo(self, ii, i)


	def clear_matrizFondo(self):

		for i in range(self.settings.filas):
			for ii in range(self.settings.columnas):
				self.matrizFondo.matriz[i][ii].valor = 0


	def instanciar_marcadores(self):

		x = int(self.settings.resolucion[0] / 1.7)
		y = 50
		gapY = 100
		size = 50

		lineas = Marcadores(self, x, y, size, 'Lineas: ', self.settings.colorMarcadores['lineas'])
		record = Marcadores(self, x, y + gapY, size, 'Record: ', self.settings.colorMarcadores['record'])
		nivel = Marcadores(self, x, y + gapY * 2, size, 'Nivel: ', self.settings.colorMarcadores['nivel'])
		self.lista_textos.add(lineas, record, nivel)


	def instancia_infoLineas(self, lineas_alavez):

		if lineas_alavez > 0:
			infolineas = infoLineas(self, lineas_alavez)
			self.lista_textos.add(infolineas)



	def instanciar_pieza(self):

		if self.settings.otraPieza:
			self.settings.otraPieza = False
			x = self.settings.xInicial
			y = self.settings.yInicial
			piezas = self.settings.piezas
			color = self.settings.colorPiezas

			nro_rnd = self.settings.next_pieza
			elegida = piezas[nro_rnd]
			idPieza = self.plantilla.pieza[elegida]
			coloresPieza = color[nro_rnd]

			# Asignar aleatoriamente la 'Next Pieza' -----
			nro_rnd = random.randrange(len(piezas))
			self.settings.next_pieza = nro_rnd
			self.verNext = nextPieza(self, self.settings.xNext, self.settings.yNext, self.plantilla.pieza[piezas[nro_rnd]], color[nro_rnd])
			# --------------------------------------------

			self.pieza = Pieza(self, x, y, idPieza, coloresPieza)
			#return self.pieza


	def actualizar_matrizFondo(self, fila):
		# Desplazar los 'rastrosPiezas' hacia abajo al hacer linea...
		filas = self.settings.filas
		columnas = self.settings.columnas

		for i in range(fila, 0, -1):
			for ii in range(columnas):
				self.matrizFondo.matriz[i][ii].valor = self.matrizFondo.matriz[i - 1][ii].valor


	def dibuja_decorados_marcos(self):

		ancho = self.settings.columnas * self.settings.tileX + 1
		alto = self.settings.filas * self.settings.tileY + 1
		pygame.draw.rect(self.pantalla, (0, 0, 0), (0, 0, ancho, alto), 1)


	def ir_al_gameOver(self):

		self.settings.estado['gameOver'] = True
		self.settings.estado['enJuego'] = False
		self.settings.sonido['gameover'].play()
		self.ultimo_update_rejugar = pygame.time.get_ticks()

		self.presentacion = gameOver(self, int((self.settings.resolucion[0] / 2) / 2), self.settings.resolucion[1] / 2, 'Game Over', 70)
		self.lista_textos.add(self.presentacion)


	def txt_rejugar(self):

		if self.settings.estado['gameOver']:
			calculo = pygame.time.get_ticks()

			if calculo - self.ultimo_update_rejugar > 5000:
				self.ultimo_update = calculo
				self.settings.estado['gameOver'] = False
				self.settings.estado['menuPrincipal'] = True
				self.pulsaComenzar = gameOver(self, int((self.settings.resolucion[0] / 2) / 2), self.settings.resolucion[1] / 1.1, 'Pulse una tecla para jugar...', 28)
				self.lista_textos.add(self.pulsaComenzar)

				self.clear_matrizFondo()
				self.settings.lineas = 0
				self.settings.nivel = 1
				self.settings.gravedad = 1100

				if self.settings.lineas > self.settings.record:
					self.settings.record = self.settings.lineas


	
	def update(self):
		pygame.display.set_caption(str(int(self.reloj.get_fps())))

		Fondo.check_lineDone(self)
		self.instanciar_pieza()

		self.lista_textos.update()
		self.txt_rejugar()

		pygame.display.flip()
		self.reloj.tick(self.settings.FPS)



	def draw(self):
		self.pantalla.fill(self.settings.colorFondo2)

		for i in range(self.settings.filas):
			for ii in range(self.settings.columnas):
				self.matrizFondo.matriz[i][ii].dibuja()

		if self.pieza:
			self.pieza.dibuja()

		nextPieza.dibuja(self, self.verNext)

		self.lista_textos.draw(self.pantalla)
		self.dibuja_decorados_marcos()
	


	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif self.settings.estado['menuPrincipal']:
					if event.key != pygame.K_UP:
						self.settings.estado['menuPrincipal'] = False
						self.settings.estado['enJuego'] = True
						self.lista_textos.remove(self.pulsaComenzar, self.presentacion)
						self.settings.sonido['click'].play()
						#pygame.mixer.music.stop()

				elif event.key == pygame.K_LEFT and self.settings.estado['enJuego']:
					self.settings.controles['izquierda'] = True

				elif event.key == pygame.K_RIGHT and self.settings.estado['enJuego']:
					self.settings.controles['derecha'] = True

				elif event.key == pygame.K_SPACE and self.settings.estado['enJuego']:
					self.settings.controles['rotar'] = True


		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_DOWN]:
			self.settings.controles['abajo'] = True

		calculo = pygame.time.get_ticks()
		if calculo - self.ultimo_update > self.settings.gravedad:
			self.ultimo_update = calculo
			self.settings.controles['abajo'] = True



	def bucle_principal(self):
		while self.settings.estado['running']:
			self.check_event()
			self.update()
			self.draw()


if __name__ == '__main__':
	game = Game()
	game.bucle_principal()

