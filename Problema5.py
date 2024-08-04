
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        
        edad_str = f", Edad: {self.edad}" if self.edad is not None else ""
        notas_str = f", Notas: {', '.join(map(str, self.notas))}" if self.notas else ""
        print(f"Nombre: {self.nombre}, Número de Registro: {self.numero_registro}{edad_str}{notas_str}")

    def setEdad(self, edad):
       
        self.edad = edad

    def setNota(self, nota):
        
        self.notas.append(nota)

alumno1 = Alumno("Abait Gamarra", "20210318A")
alumno1.setEdad(21)
alumno1.setNota(13.7)
alumno1.setNota(14.1)
alumno1.display()