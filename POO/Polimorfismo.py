class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self,largura,altura):
        self.largura = largura
        self.alura = altura
    
    def area(self):
        return self.largura * self.alura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio ** 2
    
formas = [Retangulo(5, 10), Circulo(7)]
for forma in formas:
    print(f"A área da forma é: {forma.area()}")