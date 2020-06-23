class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    alefy = Pessoa(nome='Alefy')
    thaisa= Pessoa(nome='Thaisa')
    cineide = Pessoa(alefy, thaisa, nome='Cineide')

    print(Pessoa.cumprimentar(alefy))
    print(id(alefy))
    for filho in cineide.filhos:
        print(filho.nome)
    cineide.sobrenome = 'Mesquita'
    del cineide.filhos
    print(cineide.sobrenome)
    print(cineide.__dict__)
    print(alefy.__dict__)
