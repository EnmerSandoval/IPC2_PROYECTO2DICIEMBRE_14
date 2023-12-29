class productos:
    def __init__(self, nombre, descripcion, precio, stock, codigo):
        self.nombre = nombre
        self .descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.codigo = codigo

    def mostrarInfo(self):
        print('los datos del producto son: ')
        print('nombre :' + self.nombre)
        print('descripcion :' + self.descripcion)
        print('precio :' + self.precio)
        print('stock :' + self.stock)
        print('codigo :' + self.codigo)