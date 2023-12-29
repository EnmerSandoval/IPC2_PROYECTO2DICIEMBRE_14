class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    def agregar_nodo_inicio(self, dato):
        nuevoNodo = Nodo(dato)

        #Validamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            print("Insertando nodo al principio")
            self.head.anterior = nuevoNodo
            nuevoNodo.siguiente = self.head
            self.head = nuevoNodo

    def agregar_nodo_final(self, dato):
        nuevoNodo = Nodo(dato)

        #insertamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            print("Insertando nodo al final")
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo
    

    def imprimir_lista_productos(self):
        print("*** Imprimiendo lista ***")
        # Caso de estar vacia
        if self.head is None:
            return
        nodo_temporal = self.head
        while nodo_temporal is not None:
            print(f"Codigo: {nodo_temporal.dato.codigo}")
            print(f"Nombre: {nodo_temporal.dato.nombre}")
            print(f"Descripcion: {nodo_temporal.dato.descripcion}")
            print(f"Precio: {nodo_temporal.dato.precio}")
            print(f"Stock: {nodo_temporal.dato.stock}")
            nodo_temporal = nodo_temporal.siguiente
        print()
        print('*** Fin de la lista ***')

    def imprimir_lista_clientes(self):
        print("*** Imprimiendo lista ***")
        # Caso de estar vacia
        if self.head is None:
            return
        nodo_temporal = self.head
        while nodo_temporal is not None:
            print(f"Nombre: {nodo_temporal.dato.nombre}")
            print(f"Direccion: {nodo_temporal.dato.direccion}")
            print(f"Nit: {nodo_temporal.dato.nit}")
            nodo_temp2 = nodo_temporal.dato.facturas.head
            while nodo_temp2 is not None:
                print(f"Numero factura: {nodo_temp2.dato}")
                nodo_temp2 = nodo_temp2.siguiente
            nodo_temporal = nodo_temporal.siguiente
        print()
        print('*** Fin de la lista ***')

    def imprimir_lista_facturas(self):
        print("*** Imprimiendo lista ***")
        # Caso de estar vacia
        if self.head is None:
            return
        nodo_temporal = self.head
        while nodo_temporal is not None:
            print(f"Numero factura: {nodo_temporal.dato.numero_factura}")
            print(f"Nombre: {nodo_temporal.dato.nombre}")
            print(f"Nit: {nodo_temporal.dato.nit}")
            print(f"Fecha: {nodo_temporal.dato.fecha}")
            detalle_compra = nodo_temporal.dato.detalle
            for producto in detalle_compra:
                print(f"Código: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}")
            print(f"Total: {nodo_temporal.dato.total}")
            nodo_temporal = nodo_temporal.siguiente
        print()
        print('*** Fin de la lista ***')

    def get_cliente(self, nit):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        while nodoTemporal is not None:
            # Si el dato actual es el que buscamos
            if nodoTemporal.dato.nit == nit:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        # Si ya buscamos toda la lista y no lo encontramos
        return None

    def get_producto(self, codigo_producto):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        while nodoTemporal is not None:
            # Si el dato actual es el que buscamos
            if nodoTemporal.dato.codigo == codigo_producto:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        # Si ya buscamos toda la lista y no lo encontramos
        return None

    def get_factura(self, numero_f):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        while nodoTemporal is not None:
            # Si el dato actual es el que buscamos
            if nodoTemporal.dato.numero_factura == numero_f:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        # Si ya buscamos toda la lista y no lo encontramos
        return None
    
    def get_datos(self):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        return nodoTemporal.dato
    
    