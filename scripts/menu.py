import pyxel
from batalha import combate

class menu:

    def __init__(self):
        self.opcoes = ["Jogar", "Batalhar", "Créditos", "Fechar"]
        self.opcao_selecionada = 0
        self.ativo = True
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.ativo:
            return
        
        if pyxel.btnp(pyxel.KEY_W):
            self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_S):
            self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.executar_acao()

    def draw(self):
        pyxel.cls(1)
        for i, opcao in enumerate(self.opcoes):
            cor = 10 if i == self.opcao_selecionada else 9
            pyxel.text(10, 70 + i * 10, opcao, cor)

    def executar_acao(self):
        if self.opcao_selecionada == 0:
            self.Jogar()
        elif self.opcao_selecionada == 1:
            self.Batalhar()
        elif self.opcao_selecionada == 2:
            self.Creditos()
        elif self.opcao_selecionada == 3:
            self.Fechar()

    def Jogar(self):
        return

    def Batalhar(self):
        combate()

    def Creditos(self):
        return

    def Fechar(self):
        pyxel.close()