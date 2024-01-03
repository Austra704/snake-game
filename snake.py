import random

import pygame



class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 10
    tamanho_maximo = 49 * 49

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

        self.direcao = "direita"

        self.pontos = 0

    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):

        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == "direita":
            self.corpo.insert(0, (x + self.velocidade, y))
        elif self.direcao == "esquerda":
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direcao == "cima":
            self.corpo.insert(0, (x, y - self.velocidade))
        elif self.direcao == "baixo":
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):
        if self.direcao != "baixo":
            self.direcao = "cima"

    def baixo(self):
        if self.direcao != "cima":
            self.direcao = "baixo"

    def esquerda(self):
        if self.direcao != "direita":
            self.direcao = "esquerda"

    def direita(self):
        if self.direcao != "esquerda":
            self.direcao = "direita"

    def colisao_frutinha(self, frutinha):
        return self.corpo[0] == frutinha.posicao

    def comer(self):
        self.corpo.append((0, 0))
        self.pontos = self.pontos + 1

    def colisao(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        calda = self.corpo[1:]

        return x < 0 or y < 0 or x > 490 or y > 490 or cabeca in calda or len(self.corpo) > self.tamanho_maximo

class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self, cobrinha):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.posicao = Frutinha.criar_posicao(cobrinha)

    @staticmethod
    def criar_posicao(cobrinha):
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10

        if (x, y) in cobrinha.corpo:
            Frutinha.criar_posicao(cobrinha)
        else:
            return x, y

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)



if __name__ == "__main__":
    pygame.init()
    resolucao = (500, 500)
    screen = pygame.display.set_mode(resolucao)
    pygame.display.set_caption("Snake")

    preto = (0, 0, 0)
    screen.fill(preto)
    branco = (255, 255, 255)

    cobrinha = Snake()

    frutinha = Frutinha(cobrinha)
    frutinha.blit(screen)

    fonte = pygame.font.SysFont(None, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cobrinha.cima()
                elif event.key == pygame.K_DOWN:
                    cobrinha.baixo()
                elif event.key == pygame.K_LEFT:
                    cobrinha.esquerda()
                elif event.key == pygame.K_RIGHT:
                    cobrinha.direita()

        # Verificar colisão com frutinha
        if cobrinha.colisao_frutinha(frutinha):
            cobrinha.comer()
            frutinha = Frutinha(cobrinha)

        # Verificar colisão
        if cobrinha.colisao():
            cobrinha = Snake()

        cobrinha.andar()

        screen.fill(preto)
        frutinha.blit(screen)
        cobrinha.blit(screen)

        pontuacao_texto = fonte.render(f'Pontuação: {cobrinha.pontos}', True, branco)
        screen.blit(pontuacao_texto, (10, 10))

        pygame.display.update()
        pygame.time.delay(50)  # Adiciona um pequeno atraso (50 milissegundos)





