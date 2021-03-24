import sys
import pygame
from settings import Configuracoes
from ship import Nave
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import Dados_jogo
from button import Button
from scoreboard import Pontuacao

def roda_jogo():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    raiz_config = Configuracoes()
    tela = pygame.display.set_mode((raiz_config.largura_tela, raiz_config.altura_tela))
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão de play
    botao_play = Button(raiz_config, tela, "PLAY")

    # Cria uma instância para armazenar dados do jogo e um painel de pontuação
    dados = Dados_jogo(raiz_config)
    pont = Pontuacao(raiz_config, tela, dados)

    # Cria uma nave, um grupo de balas, e um grupo de aliens
    nave = Nave(raiz_config, tela)
    balas = Group()
    aliens = Group()
    gf.cria_frota_aliens(raiz_config, tela, nave, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.responde_evento(raiz_config, tela, dados, pont, botao_play, nave, aliens, balas)
        if dados.jogo_ativo:
            nave.atualiza()
            gf.atualiza_balas(raiz_config, tela, dados, pont, nave, aliens, balas)
            gf.atualiza_aliens(raiz_config, tela, dados, pont, nave, aliens, balas)
        gf.atualiza_tela(raiz_config, tela, dados, pont, nave, aliens, balas, botao_play)

roda_jogo()