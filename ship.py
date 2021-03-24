import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, raiz_config, tela):
        """Inicializa a nave e define sua posição inicial"""
        super(Nave, self).__init__()
        self.tela = tela
        self.raiz_config = raiz_config

        # Carrega a Imagem da nave e obtém seu rect com base num retângulo, 'rect são as coordenadas que compôes a imagem'
        self.imagem = pygame.image.load('imagens/nave.bmp')
        self.rect = self.imagem.get_rect()
        self.rect_tela = tela.get_rect()

        # Inicia cada nova nave em sua posição atual, centro da tela em relação ao eixo x
        self.rect.centerx = self.rect_tela.centerx
        self.rect.bottom = self.rect_tela.bottom
        self.center = float(self.rect.centerx)
        self.mover_direita = False
        self.mover_esquerda = False

    def atualiza(self):
        """Atualiza a posição da nave de acordo com o self de movimento"""
        if self.mover_direita and self.rect.right < self.rect_tela.right:
            self.center += self.raiz_config.velocidade_nave

        if self.mover_esquerda and self.rect.left > 0:
            self.center -= self.raiz_config.velocidade_nave

        #Atualiza a rect de acordo com o self.center
        self.rect.centerx = self.center

    def  blitme(self):
        """Desenha a nave em sua posição atual"""
        self.tela.blit(self.imagem, self.rect)

    def centro_nave(self):
        """Centraliza a nave na tela"""
        self.center = self.rect_tela.centerx
