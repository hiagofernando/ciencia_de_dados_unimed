class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



class Motocicleta(veiculo):
    pass



class Carro(veiculo):
    pass



class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} estou carregado")


moto = Carro("Preta", "car-123", 2)
moto.ligar_motor()

moto = Motocicleta("Preta", "mot-123", 4)
moto.ligar_motor()

Caminhao = Caminhao("Preta", "cam-123", 18, False)
Caminhao.ligar_motor()
Caminhao.esta_carregado()
print(Caminhao)