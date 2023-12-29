import estructura
import parseo
if __name__ == '__main__':
    estructura.obtencion_datos('archivo_prueba.xml')
    detalle_factura = []
    codigo = '1001'
    cantidad = '1'
    precio = '100'
    detalle_factura.append((codigo, cantidad, precio))
    estructura.crear_factura('1001001001', 'Cliente 1', )
    parseo.generar_xml()
    