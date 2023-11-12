from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from Aplications.Usuarios.models import User
from .models import Carrito,CarritoProducto
from Aplications.productos.models import Producto
from Aplications.pedido.models import Pedido
import mercadopago
from mercadopago import *


def int(request):
    return render(request,'Carrito/carrito.html')
# Create your views here.



def carrito(request):
    if request.user.is_authenticated:
        customer = request.user
        pedido, created = Pedido.objects.get_or_create(Usuario_p=customer)
        items = pedido.carritoproducto_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'Carrito/carrito.html', context)

@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Producto ID:', productId)
    customer = request.user
    carrito = Carrito.objects.get_or_create(customer=customer)
    carrito = Carrito.objects.get(customer=customer)
    producto = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(Usuario_p=customer)
    
    carritoProducto, created = CarritoProducto.objects.get_or_create(id_pedido=pedido, id_producto=producto,id_carrito=carrito)
    
    if action == 'add':
        carritoProducto.cantidad = (carritoProducto.cantidad + 1)
    elif action == 'remove':
        carritoProducto.cantidad = (carritoProducto.cantidad - 1)
        
    carritoProducto.save()
    
    if carritoProducto.cantidad <= 0:
        carritoProducto.delete()
    
     
    
    mp = mercadopago.SDK('APP_USR-8342641464330530-111006-18e133c1779d8609de1389548914e97d-682974527')
    carritoProducto = CarritoProducto.objects.get(id_pedido=pedido, id_producto=producto, id_carrito=carrito)

    # Actualiza el total del carrito sumando los precios de todos los productos
    total_carrito = carrito.get_cart_total()
    unit_price = 1850.00         #float(carritoProducto.id_producto.precio)

    preference_data = {
        "items": [
            {
                "title": carritoProducto.id_producto.nombre,
                "quantity": carritoProducto.cantidad,
                "currency_id": "ARS",
                "unit_price":  unit_price,
            }
        ],
        "total": float(total_carrito),
    }
    preference_data_json = json.dumps(preference_data)
    print(preference_data_json)
    

    try:
        preference_response = mp.preference().create(preference_data)
        preference = preference_response["response"]
        init_point = preference["init_point"]

        print("Init Point:", init_point)
        print("Preferencia creada con éxito. ID:", preference["id"])
        return JsonResponse({'preference_id': preference["id"],'init_point':init_point})
    except IndexError as e:
        print("Error al crear la preferencia:", e)
        return JsonResponse({'error': 'Error al crear la preferencia'}, status=500)
    
    return JsonResponse('Item was added', safe=False,)


def carrito_clean(request):
    usuario_log = User.objects.get(email=request.user)
    carrito = Carrito.objects.get(customer=usuario_log.id)
    carrito.items.all().delete()
    carrito.total = 0
    carrito.save()
    return redirect(to='padre')

def carrito_delete(request, id_producto):
    
    item_carrito = CarritoProducto.objects.get(id=id_producto)
    carrito = item_carrito.id_carrito
    
    # Vuelvo a calcular el precio del carrito
    nuevo_precio_Carrito = 0 - item_carrito.id_producto.precio
    for item in carrito.items.all():
        nuevo_precio_Carrito += item.id_producto.precio

    # Realizo los cambios en la base de datos
    carrito.total = nuevo_precio_Carrito
    item_carrito.delete(id)
    carrito.save()
    return redirect(to='cart')
    
    
 