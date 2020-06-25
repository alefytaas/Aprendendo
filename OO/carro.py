from OO.motor import Motor
from OO.direcao import Direcao

class Carro():
    def __init__(self, direcao = Direcao(), motor = Motor()):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_direita(self):
        self.direcao.girar_a_direita()

    def girar_esquerda(self):
        self.direcao.girar_a_esquerda()
if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.girar_direita()
    print(carro.calcular_direcao())
    carro.motor.acelerar()

