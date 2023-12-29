import sys
import xml.etree.ElementTree as ET
from lista_doble_enlazada import *
from producto import *
from usuario import *
from fact import *
from datetime import datetime
from usuario import cliente
import json
import requests

lista_usuarios = ListaDoble()
lista_productos = ListaDoble()
lista_facturas = ListaDoble()


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
        precio_producto = float(datos.find('precio').text)
        stock_producto = int(datos.find('stock').text)
        codigo_producto = int(datos.find('codigo').text)
        print(nombre_producto)

        if lista_productos.get_producto(codigo_producto) is None:
            print('valido none para crear producto')
            producto_nuevo = Productos(nombre_producto, descripcion_producto, precio_producto, stock_producto, codigo_producto)
            lista_productos.agregar_nodo_final(producto_nuevo)
            print('agrego producto')

    for cliente in raiz.findall('clientes/cliente'):
        nombre_cliente = cliente.find('nombre').text
        nit_cliente = int(cliente.find('nit').text)
        direccion_cliente = cliente.find('direccion').text
        if lista_usuarios.get_cliente(nit_cliente) is None:
            print('valido none para crear cliente')
            cliente_nuevo = cliente(nombre_cliente, nit_cliente, direccion_cliente)
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
        Facturas.correlativo = int(numero_f)
        detalle_factura = []
        for productos in factura.findall('detalle_factura/producto'):
            codigo = productos.get('codigo')
            cantidad = int(productos.find('cantidad').text)
            precio = float(productos.find('precio').text)
            detalle_factura.append((codigo, cantidad, precio))  # <-- Aquí está el cambio
        la_factura = Facturas(nombre_cliente, nit_cliente, fecha, detalle_factura, total)
        lista_facturas.agregar_nodo_final(la_factura)

    lista_productos.imprimir_lista_productos()
    lista_usuarios.imprimir_lista_clientes()
    lista_facturas.imprimir_lista_facturas()

def crear_cliente(datos):
    try:
        nombre = datos["nombre"]
        nit = datos["nit"]
        direccion = datos["direccion"]
        if lista_usuarios.get_cliente(nit) is not None:
            print('cliente ya creado, error')
            return 400
        cliente_nuevo = cliente(nombre, nit, direccion)
        lista_usuarios.agregar_nodo_final(cliente_nuevo)
        return 200
    except ValueError:
        requests.error('Unable to parse JSON data from request.')
        return 400
    
def crear_factura(datos):
    try:
        nit = datos["nit"]
        nombre_cliente = datos["nombre"]
        detalle = datos["detalle'"]
        if lista_usuarios.get_cliente(nit) is None:
            print('no se encontro el nit del cliente, favor crearlo')
            return 400
        cliente_exsistente = lista_usuarios.get_cliente(nit)
        fecha_actual = datetime.now()
        fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
        factura_nueva = Facturas(nombre_cliente, nit, fecha_actual_str, detalle)
        total_factura = 0
        for producto in detalle:
            total_factura += float(producto[1]) * float(producto[2])
        print(total_factura)
        factura_nueva.total = total_factura
        numero_f = int(factura_nueva.numero_factura)
        cliente_exsistente.facturas.agregar_nodo_final(numero_f)
        lista_facturas.agregar_nodo_final(factura_nueva)
        return 200
    except ValueError:
        requests.error('Unable to parse JSON data from request.')
        return 400

def crear_producto(datos):
    try:
        nombre = datos["nombre"]
        descripcion = datos["descripcion"]
        precio = datos["precio'"]
        stock = datos["stock"]
        codigo = datos["codigo"]
        if lista_productos.get_producto(codigo) is not None:
            print('producto ya creado, error')
            return 400
        producto_nuevo = Productos(nombre, descripcion, precio, stock, codigo)
        lista_productos.agregar_nodo_final(producto_nuevo)
        return 200
    except ValueError:
        requests.error('Unable to parse JSON data from request.')
        return 400
    
def editar_cliente(datos):
    try:
        nombre = datos["nombre"]
        nit = datos["nit"]
        direccion = datos["direccion"]
        if lista_usuarios.get_cliente(nit) is None:
            print('no existe el cliente')
            return 400
        cliente_editar = lista_usuarios.get_cliente(nit)
        cliente_editar.nombre = nombre
        cliente_editar.direccion = direccion
        print('edito cliente')
        return 200
    except ValueError:
        requests.error('Unable to parse JSON data from request.')
        return 400

def editar_producto(datos):
    try:
        nombre = datos["nombre"]
        descripcion = datos["descripcion"]
        precio = datos["precio'"]
        stock = datos["stock"]
        codigo = datos["codigo"]
        if lista_productos.get_producto(codigo) is None:
            print('no existe el producto')
            return 400
        producto_editar = lista_productos.get_producto(codigo)
        producto_editar.nombre = nombre
        producto_editar.descripcion = descripcion
        producto_editar.precio = float(precio)
        producto_editar.stock = int(stock)
        print('edito prodcucto')
        return 200
    except ValueError:
        requests.error('Unable to parse JSON data from request.')
        return 400

def generar_xml():

    base_datos = ET.Element('base_datos')

    #creacion de productos e hijos
    productos = ET.SubElement(base_datos, 'productos')

    nodo_temporal = lista_productos.head
    print(nodo_temporal)
    while nodo_temporal is not None:
        el_producto = lista_productos.get_producto(nodo_temporal.dato.codigo)
        print(el_producto.nombre)
        producto_guardar = ET.SubElement(productos, 'producto')
        ET.SubElement(producto_guardar, 'nombre').text = el_producto.nombre
        ET.SubElement(producto_guardar, 'descripcion').text = el_producto.descripcion
        ET.SubElement(producto_guardar, 'precio').text = str(el_producto.precio)
        ET.SubElement(producto_guardar, 'stock').text = str(el_producto.stock)
        ET.SubElement(producto_guardar, 'codigo').text = str(el_producto.codigo)
        nodo_temporal = nodo_temporal.siguiente

    #creacion de clientes e hijos
    clientes = ET.SubElement(base_datos, 'clientes')

    nodo_temporal2 = lista_usuarios.head
    print(nodo_temporal2)
    while nodo_temporal2 is not None:
        el_usuario = lista_usuarios.get_cliente(nodo_temporal2.dato.nit)
        print(el_usuario.nit)
        cliente_guardar = ET.SubElement(clientes, 'cliente')
        ET.SubElement(cliente_guardar, 'nombre').text = el_usuario.nombre
        ET.SubElement(cliente_guardar, 'nit').text = str(el_usuario.nit)
        ET.SubElement(cliente_guardar, 'direccion').text = el_usuario.direccion
        facturas_cliente = ET.SubElement(cliente_guardar, 'facturas')
        nodo_temporal3 = nodo_temporal2.dato.facturas.head
        while nodo_temporal3 is not None:
            print(nodo_temporal3.dato)
            ET.SubElement(facturas_cliente, 'numero_factura').text = str(nodo_temporal3.dato)
            nodo_temporal3 = nodo_temporal3.siguiente
        nodo_temporal2 = nodo_temporal2.siguiente

    #creacion de facturas e hijos
    facturas = ET.SubElement(base_datos, 'facturas')

    nodo_temporal3 = lista_facturas.head
    print(nodo_temporal3)
    while nodo_temporal3 is not None:
        la_factura = lista_facturas.get_factura(nodo_temporal3.dato.numero_factura)
        print(la_factura.numero_factura)
        factura_guardar = ET.SubElement(facturas, 'factura')
        ET.SubElement(factura_guardar, 'nombre_cliente').text = la_factura.nombre
        ET.SubElement(factura_guardar, 'nit_cliente').text = la_factura.nit
        #fecha_actual = datetime.now()
        #fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
        ET.SubElement(factura_guardar, 'fecha').text = la_factura.fecha
        ET.SubElement(factura_guardar, 'numero_factura').text = str(la_factura.numero_factura)
        ET.SubElement(factura_guardar, 'total').text = str(la_factura.total)
        detalle_factura = ET.SubElement(factura_guardar, 'detalle_factura')
        for producto in la_factura.detalle:
            producto_xml = ET.SubElement(detalle_factura, 'producto', {'codigo': producto[0]})
            ET.SubElement(producto_xml, 'cantidad').text = str(producto[1])
            ET.SubElement(producto_xml, 'precio').text = str(producto[2])
        nodo_temporal3 = nodo_temporal3.siguiente

    arbol = ET.ElementTree(base_datos)
    arbol.write('salida_prueba.xml')

def crear_archivo():
    if os.path.exists('prueba.xml'):
        print('El archivo ya existe, porfavor cargar el archivo a la base de datos')
    else:
        try:
            with open('prueba.xml', 'x') as archivo:
                print('Archivo creado')
        except FileExistsError:
            print('El archivo ya existe, porfavor cargar el archivo a la base de datos')

def cargar():
    obtencion_datos('archivo_prueba.xml')