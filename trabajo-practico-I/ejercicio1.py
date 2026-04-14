'''Enunciado:

Modelar un sistema de transporte usando herencia y polimorfismo:

1. Crear la clase base Vehiculo con atributos marca y
velocidad_max, y método describir().

2. Crear las subclases Auto y Moto, cada una sobreescribiendo
describir() con información específica.

3. Crear una lista con al menos un Auto y una Moto, recorrerla y
llamar a describir() en cada objeto (polimorfismo).'''

class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max
        
    def describir(self):
        print(f"Marca:{self.marca}, Velocidad Maxima: {self.velocidad_max}")
    
    
class Auto(Vehiculo):
    def __init__(self, marca, velocidad_max):
        super().__init__(marca, velocidad_max)
    
    def describir(self):
        print(f"Este Auto es marca {self.marca} y cuenta con una velocidad máxima de {self.velocidad_max}")

class Moto(Vehiculo):
    def __init__(self, marca, velocidad_max):
        super().__init__(marca, velocidad_max)
        
    def describir(self):
        print(f"Esta Moto es marca {self.marca} y cuenta con una velocidad máxima de {self.velocidad_max}")
    
    
auto = Auto("Audi", "210 Km/h")
moto = Moto("Kawasaki", "280 Km/h")

# polimorfismo
vehiculos = [auto, moto]

# Recorro mi lista
for v in vehiculos:
    v.describir()

