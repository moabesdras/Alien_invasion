import pygame
from pygame.sprite import Sprite

"""Classe que administra as balas da nave"""
class Bala(Sprite):

    def __init__(self, raiz_config, tela, nave):
        """Cria um objeto para a bala, na posição atual da nave"""
        super(Bala, self).__init__()
        self.tela = tela

        # Cria um retângulo para a bala em (0,0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, raiz_config.largura_bala, raiz_config.altura_bala)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Armazena a posição da bala como um valor decimal
        self.y = float(self.rect.y)

        self.cor = raiz_config.cor_bala
        self.velocidade_bala = raiz_config.velocidade_bala

    def update(self):
        """Move a bala em direção ao topo da tela"""
        # Atualiza a posição de cima da bala
        self.y -= self.velocidade_bala

        # Atualiza a posição do rect
        self.rect.y = self.y

    def mostra_bala(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)