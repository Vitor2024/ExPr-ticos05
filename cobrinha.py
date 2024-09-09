import pygame
import random
import sys

# inicializa o pygame
pygame.init()

# Dimensões da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo da cobrinha')

# Definindo cores
verde = (0,255,0)
vermelho = (255,0, 0)
preto = (0, 0, 0)

# configurações do jogo
tamanho_celula = 20
velocidade = 15
relogio = pygame.time.clock()

# Função para gerar a comida em posição aleatoria
def gerar_comida():
    x_comida = random.randrange(0, largula, tamanho_celular)
    y_comida =_random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida

# Função para desenhar a cobrinha
def desenhar_cobrinha(cobra):
    for parte in cobra:
        pygame.draw.rect(tela, verde, (parte(0), parte(1), tamanho_celula, tamanho_celula))

        # Função principal
        def jogo():
            x= largura // 2
            y= altura // 2
            x_velocidade = 0
            y_velocidade = 0
            cobra = {(x,y)}
            comprimento_cobra = 1

            x_comida, y_comida = gerar_comida()

            while true:
                # Detecta eventos
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # captura as teclas para mover a cobrinha
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.k_LEFT and x_velocidade == 0:
                            x_velocidade = tamanho_celula
                            y
