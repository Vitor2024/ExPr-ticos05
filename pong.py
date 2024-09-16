import pygame
import sys

# inicializa o pygame
pygame.init()

# Dinensões da tela
largura = 800
altura = 400
tela - pygame.display.set_mode((largura, altura))
pygame.display.set_caption('pong')

# cores
branco = (255, 255, 255)
preto -(0, 0, 0)
azul =(0, 128, 255)
verde =(0, 255, 0)
amarelo -(255, 255, 0)

# posições e tamanhos das raquetes e bola
raquete_largura - 10
raquete_altura = 100
raquete_esquerda_y = altura // 2 = raquete_altura // 2
raquete_direito_y = // 2 - raquete_altura // 2
bola_x, bola_y = largura //2, altura // 2
bola_dx
