from django.shortcuts import render
from django.http import JsonResponse
from proyectoVacas.estructura import *
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def crearcliente(request):
    if request.method == 'POST':
        try:
            # Get the data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Process the data using your Python script
            result = crear_cliente(data)

            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def editarcliente(request):
    if request.method == 'POST':
        try:
            # Get the data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Process the data using your Python script
            result = editar_cliente(data)

            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def crearfactura(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            result = crear_factura(data)

            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@csrf_exempt        
def crearproducto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            result = crear_producto(data)

            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def obtencionDatos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            result = obtencion_datos(data)

            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def home(request):
    return render(request, 'home.html')

def clientes(request):
    return render(request, 'clientes.html')

def facturas(request):
    return render(request, 'facturas.html')

def productos(request):
    return render(request, 'producto.html')
