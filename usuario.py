import lista_doble_enlazada


class cliente:
    def __init__(self, nombre, nit, direccion):
        self.nombre = nombre
        self .direccion = direccion
        self.nit = nit
        self.facturas = lista_doble_enlazada.ListaDoble()

    def mostrarInfo(self):
        print('los datos del cliente')
        print('nombre :' + self.nombre)
        print('direccion :' + self.direccion)
        print('nit :' + self.nit)