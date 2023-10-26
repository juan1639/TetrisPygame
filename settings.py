import pygame
import random

# ----------------------------------------------------------------
# Módulo Settings.py
# 			
# ----------------------------------------------------------------
class Settings:
	def __init__(self):

		self.colorPiezas = [
	        ((255, 204, 0), (202, 162, 2), (227, 182, 2), (254, 219, 78)),
	        ((242, 55, 55), (190, 14, 14), (222, 16, 16), (244, 113, 113)),
	        ((131, 89, 149), (98, 67, 112), (121, 83, 138), (155, 117, 172)),
	        ((204, 204, 204), (166, 166, 166), (187, 187, 187), (221, 221, 221)),
	        ((159, 206, 49), (133, 172, 40), (149, 192, 46), (179, 216, 90)),
	        ((255, 174, 201), (255, 91, 145), (255, 119, 164), (255, 132, 172)),
	        ((74, 191, 240), (20, 165, 226), (52, 182, 237), (122, 207, 243))
        ]

		self.colorFondo = (73, 73, 73)
		self.colorFondo2 = (143, 127, 9)
		self.colorMarco = (70, 62, 4)
		self.colorRastroPieza = (128, 128, 128)

		self.colorMarcadores = {
			'lineas': (240, 228, 0),
			'record': (255, 206, 36),
			'nivel': (255, 130, 47)
		}

		self.resolucion = (800, 620)
		self.FPS = 60
		self.tileX = 30
		self.tileY = 30
		self.columnas = 14
		self.filas = 20

		self.xInicial = 7
		self.yInicial = 2
		self.xNext = 17
		self.yNext = 16
		self.piezas = 'zsljoit'
		self.gravedad = 1100
		self.incremento_dificultad = 10
		self.checkeando_matriz = False
		self.tiempo_infoLineas = 2000
		self.next_pieza = random.randrange(len(self.piezas))
		self.otraPieza = True

		self.lineas = 0
		self.nivel = 1
		self.record = 0

		self.controles = {
        	'izquierda': False,
        	'derecha': False,
        	'abajo': False,
        	'rotar': False,
        }

		self.estado = {
        	'running': True,
        	'menuPrincipal': False,
        	'enJuego': True,
        	'entreNiveles': False,
        	'gameOver': False
        }

		self.sonido = {
			'gameover': pygame.mixer.Sound("./sonidos/gameover.mp3"),
			'click': pygame.mixer.Sound("./sonidos/click.mp3"),
			'linea': pygame.mixer.Sound("./sonidos/disparo.mp3"),
			'musica': pygame.mixer.music
		}

