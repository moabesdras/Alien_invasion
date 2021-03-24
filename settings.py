class Configuracoes():

    def __init__(self):
        # Configurações da tela
        self.largura_tela = 900
        self.altura_tela = 600
        self.cor_fundo = (0, 0, 100)

        # Configurações da nave
        self.limite_nave = 3

        # Configurações das balas
        self.largura_bala = 3
        self.altura_bala = 15
        self.cor_bala = (0, 0, 0)
        self.qtd_balas = 3

        # Configurações dos aliens
        self.velocidade_descer_alien = 10

        # Taxa em que a velocidade do jogo aumenta
        self.escala_velocidade = 1.1

        # A taxa com que os pontos para cada alien aumenta
        self.escala_pontos = 1.5

        self.inicializa_config_dinamica()

    def inicializa_config_dinamica(self):
        """Inicializa as configurações que mudam ao decorrer do jogo"""
        self.velocidade_nave = 1.5
        self.velocidade_bala = 2
        self.velocidade_alien = 1
        # Direção da frota igual a 1 representa a direita, e -1 representa a esquerda
        self.direcao_frota = 1
        self.pontuacao_alien = 10

    def muda_velocidade(self):
        """Aumenta as configurações de velocidade"""
        self.velocidade_nave *= self.escala_velocidade
        self.velocidade_bala *= self.escala_velocidade
        self.velocidade_alien *= self.escala_velocidade

        self.pontuacao_alien = int(self.pontuacao_alien * self.escala_pontos)