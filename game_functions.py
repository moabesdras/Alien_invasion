import sys
import pygame
from bullet import Bala
from alien import Alien
from time import sleep

def responde_pressiona_tecla(evento, raiz_config, tela, nave, balas):
    if evento.key == pygame.K_d:
        nave.mover_direita = True
    elif evento.key == pygame.K_a:
        nave.mover_esquerda = True
    elif evento.key == pygame.K_KP_ENTER:
        cria_bala(raiz_config, tela, nave, balas)
    elif evento.key == pygame.K_ESCAPE:
        sys.exit()

def responde_solta_tecla(evento, nave):
    if evento.key == pygame.K_d:
        nave.mover_direita = False
    elif evento.key == pygame.K_a:
        nave.mover_esquerda = False

def responde_evento(raiz_config, tela, dados, pont, botao_play, nave, aliens, balas):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        # Move a nave para a direita ou para esquerda enquanto a tecla for pressionada
        elif evento.type == pygame.KEYDOWN:
            responde_pressiona_tecla(evento, raiz_config, tela, nave, balas)

        # Para a nave, caso a tecla seja solta
        elif evento.type == pygame.KEYUP:
            responde_solta_tecla(evento, nave)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checa_botao_play(raiz_config, tela, dados, pont, botao_play, nave, aliens, balas, mouse_x, mouse_y)

def atualiza_tela(raiz_config, tela, dados, pont, nave, aliens, balas, botao_play):
    # Redesenha a tela a cada passagem
    tela.fill(raiz_config.cor_fundo)

    # Redesenha todas as balas atrás da nave ou dos aliens
    for bala in balas.sprites():
        bala.mostra_bala()

    nave.blitme()
    aliens.draw(tela)

    # Desenha informações sobre poontuação
    pont.mostra_pontuacao()

    # Desenha o botão play, se o jogo estiver inativo
    if not dados.jogo_ativo:
        botao_play.desenha_botao()

    # Deixa a tela mais recente visível, evitando as sombras no deslocamento da nave
    pygame.display.flip()

def atualiza_balas(raiz_config, tela, dados, pont, nave, aliens, balas):
    balas.update()

    # Apaga as balas que desaparecem
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
    checa_bala_colide_alien(raiz_config, tela, dados, pont, nave, aliens, balas)

def checa_bala_colide_alien(raiz_config, tela, dados, pont, nave, aliens, balas):
    # Verifica se a bala atingiu o alien
    # Se verdade, elimina a bala e o alien
    colisao = pygame.sprite.groupcollide(balas, aliens, True, True)

    """Responde a colisão entre balas e aliens"""
    if len(aliens) == 0:
        # Se a frota toda for destruída, inicia um novo nível
        balas.empty()
        raiz_config.muda_velocidade()

        # Aumenta um nível
        dados.nivel += 1
        pont.prep_nivel()

        cria_frota_aliens(raiz_config, tela, nave, aliens)

    if colisao:
        for aliens in colisao.values():
            dados.pontuacao += raiz_config.pontuacao_alien * len(aliens)
            pont.prep_pontuacao()

        checa_pont_mxm(dados, pont)

def cria_bala(raiz_config, tela, nave, balas):
    # Cria uma bala e a adiciona ao grupo de balas
    if len(balas) < raiz_config.qtd_balas:
        nova_bala = Bala(raiz_config, tela, nave)
        balas.add(nova_bala)

def pega_qtd_linhas(raiz_config, altura_nave, altura_alien):
    # A distância da margem superior e da nave, em relação ao alien, é de 1 alien, e 2 aliens, respectivamente
    avalia_espaco_y = (raiz_config.altura_tela - (3 * altura_alien) - altura_nave)
    qtd_linhas = int(avalia_espaco_y / (2 * altura_alien))
    return qtd_linhas

def pega_qtd_aliens_x(raiz_config, largura_alien):
    """Determina o número de aliens que cabem em uma linha"""
    avalia_espaco_x = (raiz_config.largura_tela) - (2 * largura_alien)
    qtd_aliens_x = int(avalia_espaco_x / (2 * largura_alien))
    return qtd_aliens_x

def cria_alien(raiz_config, tela, aliens, alien_qtd, qtd_linhas):
    #Cria um alien e o posiciona na linha
    alien = Alien(raiz_config, tela)
    largura_alien = alien.rect.width
    # alien.x recebe a largura em que será posicionado o próximo alien em relação a margem esquerda, a cada repetição
    alien.x = largura_alien + 2 * largura_alien * alien_qtd
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * qtd_linhas
    aliens.add(alien)

def cria_frota_aliens(raiz_config, tela, nave, aliens):
    """Cria um alien e calcula o número de aliens em uma linha"""
    """O espaço entre os aliens e entre um alien e as margens é igual a largura do alien"""

    alien = Alien(raiz_config, tela)
    qtd_aliens_x = pega_qtd_aliens_x(raiz_config, alien.rect.width)
    qtd_linhas = pega_qtd_linhas(raiz_config, nave.rect.height, alien.rect.height)
    # Cria a primeira linha de aliens
    for linhas_qtd in range(qtd_linhas):
        for alien_qtd in range(qtd_aliens_x):
            cria_alien(raiz_config, tela, aliens, alien_qtd, linhas_qtd)

def checa_alien_borda(raiz_config,aliens):
    for alien in aliens.sprites():
        if alien.checa_toque_borda():
            muda_direcao_frota(raiz_config, aliens)
            break

def muda_direcao_frota(raiz_config, aliens):
    """Faz a frota descer e mudar de direção"""
    for alien in aliens.sprites():
        alien.rect.y += raiz_config.velocidade_descer_alien
    raiz_config.direcao_frota *= -1

def alien_colide_nave(raiz_config, tela, dados, pont, nave, aliens, balas):
    """Responde ao fato da nave ser atingida por um alien"""
    if dados.naves_esquerda > 0:

        # Decrementa naves_esquerda
        dados.naves_esquerda -= 1

        # Atualiza o painel de pontuações
        pont.prep_naves()

        # Esvazia a lista de aliens e balas
        aliens.empty()
        balas.empty()

        # Cria uma nova frota e centraliza a nave
        cria_frota_aliens(raiz_config, tela, nave, aliens)
        nave.centro_nave()

        # faz uma pausa
        sleep(0.5)

    else:
        dados.jogo_ativo = False
        pygame.mouse.set_visible(True)

def checa_aliens_bot(raiz_config, tela, dados, pont, nave, aliens, balas):
    """Verifica se algum alien alcançou a parte inferior da tela"""
    rect_tela = tela.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= rect_tela.bottom:
            # Trata esse caso da mesma forma que é feito qunado a nave é atingida
            alien_colide_nave(raiz_config, tela, dados, pont, nave, aliens, balas)
            break

def atualiza_aliens(raiz_config, tela, dados, pont, nave, aliens, balas):
    """Verifica se a frota está em uma das bordas e atualiza as posiçôes dos aliens"""
    checa_alien_borda(raiz_config, aliens)
    aliens.update()

    # Verifica se houve colisões entre a nave e o alien
    if pygame.sprite.spritecollideany(nave, aliens):
        alien_colide_nave(raiz_config, tela, dados, pont, nave, aliens, balas)

    # Verifica se há algum alien que atingiu a parte inferior da tela
    checa_aliens_bot(raiz_config, tela, dados, pont, nave, aliens, balas)

def checa_botao_play(raiz_config, tela, dados, pont, botao_play, nave, aliens, balas, mouse_x, mouse_y):
    """Inicia um novo jogo, quando o jogador clica em play"""
    clique_botao = botao_play.rect.collidepoint(mouse_x, mouse_y)
    if clique_botao and not dados.jogo_ativo:
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        # Reinicia os dados estatísticos do jogo
        dados.reseta_dados()
        dados.jogo_ativo = True
        raiz_config.inicializa_config_dinamica()

        #Reinicia as imagens do painel de pontuação
        pont.prep_pontuacao()
        pont.prep_pont_mxm()
        pont.prep_nivel()
        pont.prep_naves()

        # Esvazia a lista de aliens e balas
        aliens.empty()
        balas.empty()

        # Cria uma nova frota e centraliza a nave
        cria_frota_aliens(raiz_config, tela, nave, aliens)
        nave.centro_nave()

def checa_pont_mxm(dados, pont):
    """Verifica se há uma nova pontuação máxima"""
    if dados.pontuacao > dados.pont_mxm:
        dados.pont_mxm = dados.pontuacao
        pont.prep_pont_mxm()