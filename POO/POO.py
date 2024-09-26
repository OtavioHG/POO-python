class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    def obter_informacoes(self):
        return f"{self.__marca} {self.__modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.__numero_portas = numero_portas  # Atributo privado

    def obter_informacoes(self):
        return f"{super().obter_informacoes()} - {self.__numero_portas} portas"

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.__tipo = tipo  # Atributo privado

    def obter_informacoes(self):
        return f"{super().obter_informacoes()} - Tipo: {self.__tipo}"

# Exemplo de uso
veiculos = [
    Carro("Toyota", "Corolla", 4),
    Moto("Honda", "CB500", "Esportiva")
]

for veiculo in veiculos:
    print(veiculo.obter_informacoes())
