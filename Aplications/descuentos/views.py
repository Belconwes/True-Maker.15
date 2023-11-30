from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from Aplications.Usuarios.models import User
from notifcations.models import Notification
from .models import Cupon
import secrets, string
from django.contrib.auth.decorators import login_required

def generar_codigo_aleatorio(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(length))

def notificar_a_todos_los_usuarios_sobre_cupon(cupon):
    usuarios = User.objects.all()
    mensaje = f"CÓDIGO: {cupon.codigo}"
    for usuario in usuarios:
        user = usuario
        Notification.objects.create(
            actor=cupon,
            recipient=user,
            verb='¡Nuevo cupón disponible!',
            description=mensaje,
            target=cupon,
        )

@login_required
def crear_cupon(request):
    if request.method == 'POST':
        compartido = request.POST.get('compartido', False)
        codigo = request.POST.get('codigo', None)
        descuento_porcentaje = request.POST.get('porcentaje')
        print ('porcentaje:', descuento_porcentaje)
        descuento_valor = request.POST.get('valor')
        print ('valor:', descuento_valor)
        if descuento_porcentaje:
            descuento_valor=None
        if descuento_valor:
            descuento_porcentaje=None
        if not codigo:
            codigo = generar_codigo_aleatorio()
        compartido = compartido == "on"
        usuarios_asociados = request.POST.getlist('usuarios_asociados')
        
        cupon = Cupon(
            codigo=codigo,
            compartido=compartido,
            descuento_porcentaje=descuento_porcentaje,
            descuento_valor=descuento_valor)
        # ... Completa el resto de los campos y guarda el cupón
        
        # Establecer el actor como el usuario administrador actual
        cupon.actor = request.user
        cupon.save()
        # Añadir usuarios asociados si se proporcionaron en el formulario
        usuarios_asociados = request.POST.getlist('usuarios_asociados')
        for usuario_id in usuarios_asociados:
            user = User.objects.get(id=usuario_id)
            cupon.usuarios_asociados.add(user)

        if not compartido and usuarios_asociados:
            for usuario_id in usuarios_asociados:
                usuario = User.objects.get(id=usuario_id)
                mensaje = f"CÓDIGO: {cupon.codigo} (Este cupón es EXCLUSIVO)"
                Notification.objects.create(
                    actor=cupon,
                    recipient=usuario,
                    verb='¡Nuevo cupón disponible! (EXCLUSIVO)',
                    description=mensaje,
                    target=cupon,
                )
        elif compartido:
            notificar_a_todos_los_usuarios_sobre_cupon(cupon)
        
        return redirect('notificaciones_lista')

    # Renderiza la página de creación del cupón
    usuarios = User.objects.all()
    return render(request, 'descuentos/crear_cupon.html', {'usuarios': usuarios})
@login_required
def notificaciones_lista(request):
    if not request.user.is_anonymous:  # Verifica si el usuario no está autenticado
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    else:
        notifications = []
    return render(request, 'usuario/notificaciones_lista.html', {'notifications': notifications})
@login_required
def notificacion_detalle(request, notificacion_id):
    notification = get_object_or_404(Notification, id=notificacion_id)
    return render(request, 'usuario/notificacion_detalle.html', {'notification': notification})

# Create your views here.
