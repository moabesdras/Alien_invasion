import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """Classe que representa um único alien"""
    def __init__(self, raiz_config, tela):
        """Inicia o alien e define sua posição inicial"""
        super(Alien, self).__init__()
        self.tela = tela
        self.raiz_config = raiz_config

        # Carega a imagem do alien e define seu atributo rect
        self.image = pygame.image.load('imagens/nave_alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alien, pròximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alien em sua poisição atual"""
        self.tela.blit(self.image, self.rect)

    def checa_toque_borda(self):
        """Retorna True se verdade"""
        rect_tela = self.tela.get_rect()
        # Se o alien encostar no lado direito da tela
        if self.rect.right >= rect_tela.right:
            return True
        # Se o alien encostar no lado esquerdo da tela
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alien para a direita ou para a esquerda"""
        self.x += (self.raiz_config.velocidade_alien * self.raiz_config.direcao_frota)
        self.rect.x = self.x