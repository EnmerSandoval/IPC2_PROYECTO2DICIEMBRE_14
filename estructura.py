import sys
import xml.etree.ElementTree as ET
import lista_doble_enlazada
import producto
import usuario
import fact
from usuario import cliente

lista_usuarios = lista_doble_enlazada.ListaDoble()
lista_productos = lista_doble_enlazada.ListaDoble()
lista_facturas = lista_doble_enlazada.ListaDoble()


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


def pedir_ruta():
    ruta_archivo = str(input('Ingrese la ruta del archivo xml: '))
    obtencion_datos(ruta_archivo)


def obtencion_datos(ruta):
    archivo_xml = ET.parse(ruta)
    raiz = archivo_xml.getroot()

    for datos in raiz.findall('productos/producto'):
        nombre_producto = datos.find('nombre').text
        descripcion_producto = datos.find('descripcion').text
        precio_producto = datos.find('precio').text
        stock_producto = datos.find('stock').text
        codigo_producto = datos.find('codigo').text
        print(nombre_producto)

        if lista_productos.get_producto(codigo_producto) is None:
            print('valido none para crear producto')
            producto_nuevo = producto.productos(nombre_producto, descripcion_producto,
                                                precio_producto, stock_producto, codigo_producto)
            lista_productos.agregar_nodo_final(producto_nuevo)
            print('agrego producto')

    for cliente in raiz.findall('clientes/cliente'):
        nombre_cliente = cliente.find('nombre').text
        nit_cliente = cliente.find('nit').text
        direccion_cliente = cliente.find('direccion').text
        if lista_usuarios.get_cliente(nit_cliente) is None:
            print('valido none para crear cliente')
            cliente_nuevo = usuario.cliente(nombre_cliente, nit_cliente, direccion_cliente)
            lista_usuarios.agregar_nodo_final(cliente_nuevo)
        for factura in cliente.findall('facturas/numero_factura'):
            print('entro a buscar numero factura')
            numero_f = factura.text
            print('numero factura a almacenar; ', numero_f)
            el_cliente = lista_usuarios.get_cliente(nit_cliente)
            el_cliente.facturas.agregar_nodo_final(int(numero_f))  # corregí aquí

    for factura in raiz.findall('facturas/factura'):
        nombre_cliente = factura.find('nombre_cliente').text
        nit_cliente = factura.find('nit_cliente').text
        fecha = factura.find('fecha').text
        numero_f = factura.find('numero_factura').text
        total = float(factura.find('total').text)
        fact.Facturas.correlativo = int(numero_f)
        detalle_factura = []
        for productos in factura.findall('detalle_factura/producto'):
            codigo = productos.get('codigo')
            cantidad = int(productos.find('cantidad').text)
            precio = float(productos.find('precio').text)
            detalle_factura.append((codigo, cantidad, precio))  # <-- Aquí está el cambio
        la_factura = fact.Facturas(nombre_cliente, nit_cliente, fecha, detalle_factura,total)
        lista_facturas.agregar_nodo_final(la_factura)

    lista_productos.imprimir_lista_productos()
    lista_usuarios.imprimir_lista_clientes()
    lista_facturas.imprimir_lista_facturas()


def crear_cliente(nombre_cliente, nit_cliente, direccion_cliente):
    cliente_nuevo = usuario.cliente(nombre_cliente, nit_cliente, direccion_cliente)
    lista_usuarios.agregar_nodo_final(cliente_nuevo)
    print('agrego cliente')


def crear_factura(nit_cliente, nombre_cliente, detalle_factura, fecha):
    if lista_usuarios.get(nit_cliente) is None:
        print('no se encontro el nit del cliente, favor crearlo')
        return
    cliente_exsistente = lista_usuarios.get(nit_cliente)
    factura_nueva = fact.Facturas(nombre_cliente, nit_cliente, fecha, detalle_factura)
    cliente_exsistente.Facturas.agregar_nodo_final(factura_nueva)
    lista_facturas.agregar_nodo_final(factura_nueva)
