import pygame.font #Basicamente, tranforma um texto em uma imagem

class Button():

        def __init__(self, raiz_config, tela, msg):
            """Inicializa os atributos do botão"""
            self.tela = tela
            self.rect_tela = tela.get_rect()

            # Define as dimensões e propriedades do botão
            self.largura = 200
            self.altura = 50
            self.cor_botao = (0, 255, 0)
            self.cor_texto = (0, 0, 0)
            self.fonte = pygame.font.SysFont(None, 48)

            # Constrói o objeto rect do botão, e o centraliza
            self.rect = pygame.Rect(0, 0, self.largura, self.altura)
            self.rect.center = self.rect_tela.center

            # A mensagem do botão deve ser preparada apenas uma vez
            self.prepara_msg(msg)

        def prepara_msg(self, msg):
            """Transforma msg em uma imagem renderizada e centraliza o texto no botão"""
            self.imagem_msg = self.fonte.render(msg, True, self.cor_texto, self.cor_botao)
            self.rect_imagem_msg = self.imagem_msg.get_rect()
            self.rect_imagem_msg.center = self.rect.center

        def desenha_botao(self):
            """Desenha uma o botão e depois insere a mensagem"""
            self.tela.fill(self.cor_botao, self.rect)
            self.tela.blit(self.imagem_msg, self.rect_imagem_msg)