class Dados_jogo():

    """Armazena dados do jogo"""
    def __init__(self, raiz_config):
        """Inicializa os dadso estatísticos"""
        self.raiz_config = raiz_config
        self.reseta_dados()
        self.jogo_ativo = False
        # A pontuação máxima jamais será reiniciada
        self.pont_mxm = 0

    def reseta_dados(self):
        """Inicializa os dados que podem mudar durante o jogo"""
        self.naves_esquerda = self.raiz_config.limite_nave
        self.pontuacao = 0
        self.nivel = 1