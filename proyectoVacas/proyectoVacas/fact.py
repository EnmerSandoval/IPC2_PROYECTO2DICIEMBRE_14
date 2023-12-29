import os
class Facturas:
    correlativo = 1
    def __init__(self, nombre_cliente, nit_cliente, fecha, detalle_compra,total):
        self.nombre = nombre_cliente
        self.nit = nit_cliente
        self.fecha = fecha
        self.detalle = detalle_compra
        self.total = total
        self.numero_factura = Facturas.correlativo
        Facturas.correlativo += 1

    @staticmethod
    def cargar_correlativo():
        if os.path.exists("correlativo.txt"):
            with open("correlativo.txt", "r") as f:
                Facturas.correlativo = int(f.read())

    @staticmethod
    def guardar_correlativo():
        with open("correlativo.txt", "w") as f:
            f.write(str(Facturas.correlativo))

    def mostrarInfo(self):
        print('los datos de la factura son: ')
        print('nombre :' + self.nombre)
        print('nit :' + self.nit)
        print('fecha :' + self.fecha)
        print('detalle: ' + self.detalle)