from django.shortcuts import render,redirect
from .models import User
from Aplications.productos.models import Producto,Categoria
from .forms import Userform,Authformi
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.template import loader
# Create your views here.
def prueba(request):
    tabla = Userform
    
    return render (request,'Main.html',{'form': tabla})

def home(request):
    category = Categoria.objects.all()
    products = Producto.objects.all()
    if request.method == 'POST':
        
        
        return render(request,'Main.html',{'product':products,'cata' : category},id)
    else:
         
        return render(request,'Main.html',{'product':products,'cata' : category})


def User_regist(request):
    tabla = Userform()
    
    if request.method == 'GET':
        print('Obteiendo datos')
        return render(request,'Registros/base-signup.html',{'form':tabla})
    else:
        #Comprobacion de si los textbox tienen el mismo password
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(email=request.POST['email'],nombre=request.POST['nombre'] ,apellido=request.POST['apellido'],password=request.POST['password1'])
                print(request.POST)
                user.save()
                login(request,user)
                print('Si envia')
                subject = "Prueba de envio Email a un correo no asociado a la cuenta Host user"
                message = "este mail es de prueba para ver si funciona el envio de emails dentro de un form"
                from_mail = settings.EMAIL_HOST_USER
                listdescrip = ["gaunaabeltiago@gmail.com"]
                send_mail(subject, message, from_mail, listdescrip)
                return redirect('padre')
            except IntegrityError:
                print('Recibiendo datos')
                error = 'Usuario ya registrado intente con otro'
                return render(request,'Registros/register.html',{'form':tabla,'error':error})
            
        return render(request,'Registros/base-signup.html',{'form':tabla,'error':'No coinciden passwords'})



def init(request):
    if request.method == 'GET':
        aut = Authformi
        print('terrible ayuda')
        return render(request,'Registros/base-signup.html',{'form':aut})
    else:
         user = authenticate(request,email=request.POST['email'],password=request.POST['password'])
       
         if user is None:
             aut = Authformi
             return render(request,'Registros/base-signup.html',{'form':aut,'error': 'NO gay no exite'})
         else:
           login(request,user)
           messages.success(request,"iniaciado correct")
           return redirect('padre')
        
        
        


def log_out(request):
    logout(request)
    
    return redirect('padre')

#Pruebas send mail con el host Gmail
def proba(request):
    return render(request,'old.html')

def tomail(request):
    if request.method == 'GET':
        print('No envia')
        return render(request,'old.html')
    else:
         print('Si envia')
         subject = "Prueba de envio Email a un correo no asociado a la cuenta Host user"
         message = "este mail es de prueba para ver si funciona el envio de emails dentro de un form"
         from_mail = settings.EMAIL_HOST_USER
         listdescrip = ["piericarp03@gmail.com"]
         send_mail(subject, message, from_mail, listdescrip)
         return render(request,'old.html')


def carta(request):
    return render(request,'cards/carta.html')