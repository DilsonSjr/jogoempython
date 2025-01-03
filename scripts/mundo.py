import pyxel
import time
from jogador import Personagem
from inimigo import Inimigo
from NPC import NPC
from batalha import Combate

class Porta:
    def __init__(self, x1, y1, x2, y2, largura=16, altura=16, cooldown=1):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.largura, self.altura = largura, altura
        self.cooldown = cooldown
        self.ultimo_uso = -cooldown  # pra ele nao poder entrar direto na porta

    def verificar_porta(self, jogador):
        tempo_atual = time.time()

        if tempo_atual - self.ultimo_uso < self.cooldown:# Verifica se o cooldown já passou
            return

        # Verifica se o jogador está na área da primeira porta pra nao ter que ser um pixel especifico
        if self.x1 <= jogador.x < self.x1 + self.largura and self.y1 <= jogador.y < self.y1 + self.altura:
            jogador.x, jogador.y = self.x2, self.y2
            self.ultimo_uso = tempo_atual  # Atualiza o tempo do último uso
            print(f"Entrou na porta de ({self.x1}, {self.y1}) para ({self.x2}, {self.y2})")

        elif self.x2 <= jogador.x < self.x2 + self.largura and self.y2 <= jogador.y < self.y2 + self.altura:
            jogador.x, jogador.y = self.x1, self.y1
            self.ultimo_uso = tempo_atual  # Atualiza o tempo do último uso
            print(f"Entrou na porta de ({self.x2}, {self.y2}) para ({self.x1}, {self.y1})")

class Mapa:
    def __init__(self, jogador):
        pyxel.load('../assets/images/bartolomeu.pyxres')   
        #pyxel.playm(0, 1, True)  # Toca a música de fundo
        self.inimigo = Inimigo(235, 194)

############ Posições das portas        
        self.portas = [
            Porta(1036, 207, 130, 450), # casa do player
            Porta(1081, 558, 310, 367), # GIM (ginasio)
            Porta(452,352,1337,239), # Miaws (mercadinho)
        ]

############ desenha os NPCS
        self.npcs = [
            NPC(268,377, "Iae cara, voce e novo aqui nao e ?", 0, 176, 16, 16, num_quadros=4, intervalo_animacao=0.2),
            NPC(280,400, "Cara eu ate queria sair da Gatopolis,\nmas o tutui guarda a chave do portão", 16, 192, 16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(296,400, "tutui é o gato mais forte daqui,\nvive na academia", 48, 208, -16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(1071,350, "EU SOU O TUTUI O LARGATAO\nE EU MANDO NESSE LUGAR", 128, 192, 16, 16, num_quadros=3, intervalo_animacao=0.1),
            NPC(440,398, "ai que delicia esse picole", 64, 176, 16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(294,246, "Uma caixinha de papelao\nera meu sonho agora", 0, 240, 16, 16, num_quadros=3, intervalo_animacao=0.1),
            NPC(600,200, "Cerebros,\n cerebros fresquinhos,\neu quero cerebros fresquinhossss", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(244,500, "eu juro proce, Gatopolis instiga\ntodo mundo a falar errado", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(211,530, "eu to ocupado tentando nao falar com voce ok?\nsai fora", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(210,577, "EQUIPAR UM ITEM FAZ VOCE FICAR MAIS FORTE\ndesculpa eu sempre quis ser tutorial \nde um jogo em vida", 0, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(215,587, "qui saudadi de passa o dia todo fazendo nada so\n ZzZ", 64, 208, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(278,610, "virei policial aqui so pelo distintivo brilhante", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(436,704, "queria entra pra academia,\nmas o tutui so deixa os de verdade la", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(578,756, "queria comprar um terninho\nmas eu sou tao pobrin", 0, 208, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(534,844, "nao fala comigo nao que\neu to trevoso", 0, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(475,844, "nao, olhe, para a luz vermelha", 0, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(368,878, "nao tem um inseto pra cacar\nque odio", 0, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(268,774, "novelo di la\num item di luxo por essas bandas\nsim", 128, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(376,384, "hey toma cuidado,\nexistem gatos perigosos por aqui", 112, 224, -16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(132,212, "ai eu adoro praia, mas essa areia te conta", 64, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(548,134, "essa cidade e muito BRAT meo", 64, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(613,126, "aquele portao dourado, e a saida de gatopolis,\ndizem que tudo e possivel apartir dele ", 0, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(687,283, "ei amor olha aquele peixe la", 0, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(687,300, "se eu tivesse uma vara de pesca\nele ja tava fritin", 64, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(415,423, "Verdade que picole bom, é de frango?", 64, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(589,501, "queria ir no show da Miewllie catish\nvoce conhece? ela canta\n\nmeaw, meaw, meaw", 64, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(627,547, "ei me conta como vc veio parar aqui?", 128, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            
            
                    ]
        self.jogador = jogador

        pyxel.run(self.update, self.draw)
        pyxel.run(self.update, self.draw)

    def update(self):

    # Atualiza cada NPC
        for npc in self.npcs:
            npc.detectar_jogador(self.jogador)

        self.jogador.mover()


        # Verifica passagem para cada porta
        for porta in self.portas:
            porta.verificar_porta(self.jogador)

        # Log pra debug das posições (usando pra saber as posiçoes das portas)
        print(f"Posição do jogador: ({self.jogador.x}, {self.jogador.y})")

        # Verifica se as posições do jogador e do inimigo coincidem
        if (self.jogador.x == self.inimigo.x and self.jogador.y in range(self.inimigo.y - 50, self.inimigo.y + 50)) or \
            (self.jogador.y == self.inimigo.y and self.jogador.x in range(self.inimigo.x - 50, self.inimigo.x + 50)):
            Combate(self.jogador, self.inimigo, self)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 2000, 2000) #mapa tem que ser enorme pra caber as casas do lado de fora do mapa
        self.inimigo.desenhar()
        self.jogador.desenhar()

# Desenha cada NPC
        for npc in self.npcs:
            npc.desenhar()

    def retornar_ao_mundo(self):
        pyxel.run(self.update, self.draw)
