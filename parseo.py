import os
import xml.etree.ElementTree as ET
import estructura
from datetime import datetime

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
    estructura.obtencion_datos('archivo_prueba.xml')

def generar_xml():

    base_datos = ET.Element('base_datos')

    #creacion de productos e hijos
    productos = ET.SubElement(base_datos, 'productos')

    nodo_temporal = estructura.lista_productos.head
    print(nodo_temporal)
    while nodo_temporal is not None:
        el_producto = estructura.lista_productos.get_producto(nodo_temporal.dato.codigo)
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

    nodo_temporal2 = estructura.lista_usuarios.head
    print(nodo_temporal2)
    while nodo_temporal2 is not None:
        el_usuario = estructura.lista_usuarios.get_cliente(nodo_temporal2.dato.nit)
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

    nodo_temporal3 = estructura.lista_facturas.head
    print(nodo_temporal3)
    while nodo_temporal3 is not None:
        la_factura = estructura.lista_facturas.get_factura(nodo_temporal3.dato.numero_factura)
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
