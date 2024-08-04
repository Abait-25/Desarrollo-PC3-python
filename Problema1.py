"""
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:

"""
def Funcionxy():
  try: 
     X=int(input("digite X: "))
     Y=int(input("Digite Y: "))
     porcentage=(X/Y)*100
     porcentage=round(porcentage)
     if porcentage <= 1:
        print("estado: E")
     elif porcentage>=99 and porcentage<=100 :
        print("Estado: F")
     elif porcentage>=100 :
        print("error, x>y !!!")
        raise Exception 
     else:
        print(f"{porcentage}% ")
  except ValueError:
     print("ocurrio un problema(digite solo enteros)")
  except ZeroDivisionError:
     print("ocurrio un problema, repitalo")
     return Funcionxy()
Funcionxy()













