"""
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
Cree 2 objetos de tipo circulo y calcule su área.
"""
import math

class CIRCULO:
    def __init__(self, radio):
      self.radio=radio
    def area(self):
       self.areas=math.pi*self.radio*self.radio
       print(f"area circulo: {self.areas}")

    def __str__(self):
      return f" Circulo con Radio :{self.radio} "