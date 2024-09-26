class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
cachorro = Cachorro("Rex", 5)
gato = Gato("Mia", 3)
print(f"{cachorro.nome} tem {cachorro.idade} anos e faz: {cachorro.fazer_som()}")
print(f"{gato.nome} tem {gato.idade} anos e faz: {gato.fazer_som()}")