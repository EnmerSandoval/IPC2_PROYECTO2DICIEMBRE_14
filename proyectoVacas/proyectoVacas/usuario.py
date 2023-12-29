from proyectoVacas.lista_doble_enlazada import *

class cliente:
    def __init__(self, nombre, nit, direccion):
        self.nombre = nombre
        self .direccion = direccion
        self.nit = nit
        self.facturas = ListaDoble()

    def mostrarInfo(self):
        print('los datos del cliente')
        print('nombre :' + self.nombre)
        print('direccion :' + self.direccion)
        print('nit :' + self.nit)