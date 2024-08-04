"""
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)

"""

lista=input("Digite calificaciones separadas por coma: ")

try:
    notas=lista.split(",")
    calificaciones=[]
    n=len(notas)
    i=0

    while i < n:
        notas[i]=int(float(notas[i]))
        calificaciones.append(notas[i])
        i=i+1
    print(calificaciones)
except:
    print("los valores introducidos no puedan ser convertidos debido a un error de tipeo o formato")
