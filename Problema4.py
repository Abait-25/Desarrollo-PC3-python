"""
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un
objeto de tipo rectangulo y 1 de tipo cuadrado.
"""
class RECTANGULO:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho  
    def area(self):
        self.area=self.largo*self.ancho
        print(f"Area :{self.area} ")
    def __str__(self):
        return f"Rectangulo con Ancho: {self.ancho} y Largo: {self.largo} "

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.lado = lado
    def __str__(self):
        return f"Cuadrado con lado: {self.lado}"


rectangulo1=RECTANGULO(5,3)
print(rectangulo1)
rectangulo1.area()

cuadrado1=CUADRADO(3)
print(cuadrado1)
cuadrado1.area()
