"""
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades.
Cree 3 objetos de tipo producto y agregalos al catálogo. Colocar ejemplos empleandolos
métodos de catálogo.

"""
class Producto:
    def __init__(self,nombre,marca,año):
        self.nombre=nombre
        self.marca=marca
        self.año=año
    def __str__(self):
        return f" Nombre: {self.nombre} , Marca: {self.marca}, Año: {self.año}"
    
producto1=Producto("Motor", "Stanley", 2023)
producto2=Producto("Cadena", "Stanley", 2023)
producto3=Producto("Refrigerante", "Knex", 2020)


class Catalogo:
    productos = []
    def __init__(self, producto=[]):
      self.producto=producto
    def agregar(self,p):
      self.producto.append(p)
    def mostrar(self):
        for p in self.producto:
            print(p)  # Print toma por defecto str(p)
    def buscar_producto(self, Var_año):
        for producto in self.producto:
            if producto.año == Var_año:
                break
        return producto
    def buscar_marca(self, Var_marca):
        for producto in self.producto:
            if producto.marca == Var_marca:
                break
        return producto
    def __str__(self):
       return f"Catalogo:  con producto {self.producto}"

cat1=Catalogo([producto1,producto2, producto3])
cat1.mostrar()
print(cat1.buscar_producto(2020))
print(cat1.buscar_marca("Stanley"))
