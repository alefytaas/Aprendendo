class Pessoa:
    def __init__(self, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    p = Pessoa('Alefy')
    print(Pessoa.cumprimentar(p))
    print(id(p))
