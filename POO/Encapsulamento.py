class ContaBancaria():
    def __init__(self, slado_inicial):
        self.__slado = slado_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__slado += valor
            print(f"Deposito de {valor} realizado. Saldo atual: {self.__slado}.")
        else:
            print("Vc nao pode adicionar valor negativo")

    def sacar(self, valor):
        if valor <= self.__slado:
            self.__slado -= valor
            print(f"Saque de {valor} relizado. Saldo atual: {self.__slado}")
        else:
            print("saldo insuficiente ")

    def obter_saldo(self):
        return self.__slado
    
conta = ContaBancaria(100)
conta.depositar(int(input("Qual vai ser seu deposito: ")))
conta.sacar(int(input("Qual vai ser o valor do se sacer: ")))
print(f"Saldo final: {conta.obter_saldo()}.")

