'''Enunciado:

Crear una clase base Figura con atributo color y método area() que
retorne 0.

Crear las subclases Rectangulo (base, altura) y Circulo (radio),
sobreescribiendo area() en cada una con la fórmula
correspondiente.

Agregar el método describir() en la clase base que imprima color y
area, y verificar que el polimorfismo funcione'''

import math #esto es para poder usar pi luego

class Figura:
    def __init__(self, color):
        self.color= color
        
    def area(self):
        return 0
    
    def describir(self):
        print(f"Color: {self.color} | Area: {self.area()}")
    
class Rectangulo(Figura):
    def __init__(self, color,base,altura):
        super().__init__(color)
        self.base = base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura

class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio = radio
        
    def area(self):
        return math.pi * self.radio**2
    
    
rectangulo = Rectangulo(" rectangulo rojo",13, 19)
circulo = Circulo("circulo verde",23)

# polimorfismo
figuras = [rectangulo, circulo]

# Recorro mi lista
for x in figuras:
    x.describir()