import os

def crear_archivo():
    if os.path.exists('prueba.xml'):
        print('El archivo ya existe')
        cargar()
    else:
        try:
            with open('prueba.xml', 'x') as archivo:
                print('Archivo creado')
        except FileExistsError:
            print('El archivo ya existe')
            cargar()

def cargar():
    # Código para cargar el archivo
    pass

# Llamada al método para crear el archivo
crear_archivo()