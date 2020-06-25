class Direcao():

    def __init__(self, valor = 'Norte'):
        self.valor = valor

    def girar_a_direita(self):
        if self.valor == "Norte":
            self.valor='Leste'
        elif self.valor=='Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if self.valor=='Norte':
            self.valor='Oeste'
        elif self.valor=='Leste':
            self.valor = 'Norte'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'