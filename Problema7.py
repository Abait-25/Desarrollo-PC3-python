"""
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
"""
import math
class Punto:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
    def cuadrante(self):
        if self.X >0 and self.Y>0:
           print("Punto pertenece a: 1er cuadrante ")
        elif self.X<0 and self.Y<0:
            print("Punto pertenece a: 3er cuadrante ")
        elif self.X<0 and self.Y>0:
            print("Punto pertenece a: 2do cuadrante ")
        elif self.X>0 and self.Y>0:
            print("Punto pertenece a: 4to cuadrante ") 
        else:
            print("Punto pertenece a algunos de los ejes ") 
    def Vector(self, x2, y2):
        self.x2=x2
        self.y2=y2
        print(f"Vector resultante con el punto  (X2,Y2)=({self.x2},{self.y2}) \n → vector=({self.x2-self.X},{self.y2-self.Y}) ")
    def Distancia(self,a3,b3):
        self.a3=a3
        self.b3=b3
        distancia=math.sqrt((self.a3 - self.X)**2 + (self.b3 - self.Y)**2)
        print(f" Distancia con el punto :({self.a3},{self.b3}) → distancia={distancia} ")

    def __str__(self):
        return f"Punto A : (X,Y)= ({self.X},{self.Y}) "


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def base(self):
        return abs(self.punto2.X - self.punto1.X)
    
    def altura(self):
        return abs(self.punto2.Y - self.punto1.Y)
    
    def area(self):
        return self.base() * self.altura()
    
    def __str__(self):
        return f"Rectángulo con base = {self.base()} y altura = {self.altura()}"

"""
 A(2, 3), B(5,5), C(-3, -1) y D(0,0)
"""
puntoA = Punto(2, 3)
puntoB = Punto(5, 5)
puntoC = Punto(-3,-1)
puntoD = Punto(0,0)

puntoA.cuadrante()
puntoC.cuadrante()
puntoD.cuadrante()

puntoA.Vector(5, 5)
puntoB.Vector(2,3)

puntoA.Distancia(5,5)
puntoB.Distancia(2,3)

Rectangulo(puntoA,puntoB)
print(Rectangulo(puntoA,puntoB))
print(Rectangulo(puntoA,puntoB).area())