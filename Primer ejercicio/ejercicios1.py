from abc import ABC, abstractmethod #esto le pedi ayuda a claude porque no recordaba como traer el metodo abstracto

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_sueldo(self):
        pass

    def mostrar_datos(self):
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo Base {self.salario_base}")

#el empleado contratado combra unicamente por hora
class EmpleadoContratado(Empleado):
    def __init__(self, nombre, salario_base, valor_hora, horas_trabajadas):
        super().__init__(nombre, salario_base)
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self.salario_base + (self.valor_hora * self.horas_trabajadas)

    def actualizar_datos(self, nuevas_horas):
        self.horas_trabajadas = nuevas_horas

    def mostrar_horas(self):
        print(f"Horas trabajadas: {self.horas_trabajadas}")


# Clase EmpleadoFijo cobra sueldo fijo mas bono de antiguedad
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario_base, bono_antiguedad):
        super().__init__(nombre, salario_base)
        self.bono_antiguedad = bono_antiguedad

    def calcular_sueldo(self):
        return self.salario_base + self.bono_antiguedad

    def actualizar_datos(self, nuevo_bono):
        self.bono_antiguedad = nuevo_bono

    def mostrar_bono(self):
        print(f"Bono de antigüedad: {self.bono_antiguedad}")


empleado1 = EmpleadoContratado("Juan Rodriguez", 0, 20000, 50)
empleado2 = EmpleadoFijo("Ana Gonzalez", 1000000, 500000)

print("-----------------------------------")
print("Empleado Contratado:")
empleado1.mostrar_datos()
empleado1.mostrar_horas()
print("Sueldo:", empleado1.calcular_sueldo())

print("-----------------------------------")
print("Empleado Fijo:")
empleado2.mostrar_datos()
empleado2.mostrar_bono()
print("Sueldo:", empleado2.calcular_sueldo())