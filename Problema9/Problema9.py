import prob3
import prob4
"""
Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
menú para utilizar deberá tener las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.
Deberá emplear un método que valide que los datos ingresados sean números validos y
positivos en caso corresponda.


"""
print("MENU")
print("1. Calcular el área de un circulo \n2. Calcular el área de un rectangulo \n3. Calcular el área de un cuadrado \n4. Salir.")

respuesta=input("Digite su opcion: ")

        
try:
    if respuesta=='1':
        x=float(input("digite el radio: "))
        area=prob3.CIRCULO(x).area()
    elif respuesta=='2':
        x=float(input("digite un lado del rectangulo: "))
        y=float(input("digite otro lado del rectangulo: "))
        area=prob4.RECTANGULO(x,y).area()
    elif respuesta=='3':
        x=float(input("digite el lado del cuadrado: "))
        area=prob4.CUADRADO(x).area()
    elif respuesta=='4':
        print("Programa terminado")
    else:
        print("respuesta no valida, intentelo otra vez")

except ValueError:
     print("Error, digite bien el numero")

