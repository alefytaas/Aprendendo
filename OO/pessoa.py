class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} olhos {cls.olhos}'

class Homem(Pessoa):
    pass



if __name__ == '__main__':
    alefy = Homem(nome='Alefy')
    thaisa= Pessoa(nome='Thaisa')
    talles = Pessoa(nome='Talles')
    cineide = Pessoa(alefy, thaisa, talles, nome='Cineide')

    print(isinstance(alefy, Pessoa))
    print(Pessoa.cumprimentar(alefy))
    print(id(alefy))
    for filho in cineide.filhos:
        print(filho.nome)
    cineide.sobrenome = 'Mesquita'
    del cineide.filhos
    print(cineide.sobrenome)
    print(cineide.__dict__)
    print(alefy.__dict__)
    print(Pessoa.olhos)
    print(alefy.olhos)
    print(Pessoa.metodo_estatico(), alefy.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())

