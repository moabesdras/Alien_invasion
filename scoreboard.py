import pygame.ftfont
from pygame.sprite import Group
from ship import Nave

class Pontuacao():
    """Classe para mostrar informações sobre a pontuação"""

    def __init__(self, raiz_config, tela, dados):
        """Inicializando a pontuação"""
        self.tela = tela
        self.rect_tela  = tela.get_rect()
        self.raiz_config = raiz_config
        self.dados = dados

        # Configurações de formatação
        self.cor_texto = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem das pontuações iniciais
        self.prep_pontuacao()
        self.prep_pont_mxm()
        self.prep_nivel()
        self.prep_naves()

    def prep_pontuacao(self):
        """Tranforma a pontuação em uma imagem renderizada"""
        arredonda_pontuacao = int(round(self.dados.pontuacao, -1))
        pontuacao_str = "{:,}".format(arredonda_pontuacao)
        self.pontuacao_imagem = self.font.render(pontuacao_str, True, self.cor_texto, self.raiz_config.cor_fundo)

        # Exibe a pontuação na parte superior da tela
        self.pontuacao_rect = self.pontuacao_imagem.get_rect()
        self.pontuacao_rect.right = self.rect_tela.right - 20
        self.pontuacao_rect.top = 20

    def prep_pont_mxm(self):
        """Transforma a pontuação máxima em uma imagem renderizada"""
        pont_mxm = int(round(self.dados.pont_mxm, -1))
        pont_mxm_str = "{:,}".format(pont_mxm)
        self.pont_mxm_imagem = self.font.render(pont_mxm_str, True, self.cor_texto, self.raiz_config.cor_fundo)

        # Centraliza a pontuação máxima na parte superior da tela
        self.rect_pont_mxm = self.pont_mxm_imagem.get_rect()
        self.rect_pont_mxm.centerx = self.rect_tela.centerx
        self.rect_pont_mxm.top = self.pontuacao_rect.top

    def mostra_pontuacao(self):
        self.tela.blit(self.pontuacao_imagem, self.pontuacao_rect)
        self.tela.blit(self.pont_mxm_imagem, self.rect_pont_mxm)
        self.tela.blit(self.nivel_imagem, self.rect_nivel)

        # Desenha as naves
        self.naves.draw(self.tela)

    def prep_nivel(self):
        """Tranforma o nível em uma imagem renderizada"""
        self.nivel_imagem = self.font.render(str(self.dados.nivel), True, self.cor_texto, self.raiz_config.cor_fundo)
        # Posiciona o nível abaixo da pontuação
        self.rect_nivel = self.nivel_imagem.get_rect()
        self.rect_nivel.right = self.pontuacao_rect.right
        self.rect_nivel.top = self.pontuacao_rect.bottom + 10

    def prep_naves(self):
        """Mostra quantas naves restam"""
        self.naves = Group()
        for num_naves in range(self.dados.naves_esquerda):
            nave = Nave(self.raiz_config, self.tela)
            nave.rect.x = 10 + num_naves * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)