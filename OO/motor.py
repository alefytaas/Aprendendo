class Motor():
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade+=1

    def frear(self):
        if self.velocidade>-1:
            self.velocidade= self.velocidade-3
            if self.velocidade<-1:
                self.velocidade=-1
        else:
            print("""Carro parado""")