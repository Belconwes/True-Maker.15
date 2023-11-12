from django.shortcuts import render,redirect,get_object_or_404
from Aplications.productos.models import Producto,Categoria
from Aplications.Usuarios.views import home
from .forms import Producto_f

def cart(request,id):
    
    productos = Producto.objects.filter(id=id)
    
    print(productos)
    
    
    return render(request,'productos/detail_p.html',{'productos':productos})


def carga_p(request):
    try:
        if request.method == 'GET':
            prod = Producto_f()
            return render(request,'productos/carga_p.html',{'form':prod})
        else:
            prod = Producto_f(data=request.POST,files=request.FILES)
            if prod.is_valid():
                print('pasa')
                prod.save()
                return redirect(to='padre')
                
            else:
               print('No funciona')
               return render(request,'productos/carga_p.html',{'form':prod})
                 
    except ValueError as i:
        print(i)



def modify_p(request,id):
    products = get_object_or_404(Producto,id=id)
    try:
        if request.method == 'GET':
            data ={
                'form': Producto_f(instance=products) 
            }
            return render (request,'productos/modificar.html',data)
        else:
            products = get_object_or_404(Producto,id=id)
            formulario = Producto_f(data=request.POST,instance=products,files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                print('valid')
                return redirect(to='padre')
    except ValueError as e:
        print(e)
        
def search(request):
    text_search = request.GET['texto']
    products_to_name = Producto.objects.filter(nombre__icontains=text_search).all()
    products_to_descripcion = Producto.objects.filter(descripcion__icontains=text_search).all() 
    products = products_to_name | products_to_descripcion
    return render(request,'productos/search.html',
    {
                      
        'categorias' : Categoria.objects.all(),
        'productos' : products,
        'texto_buscado' : text_search,
        'titulo_seccion' : 'Productos que contienen',
        'sin_productos': 'No hay producto de la categoria ' + text_search
    })           
    

def search_c(request,categoria_id):
    categoria = get_object_or_404(Categoria,id = categoria_id)
    Categoria_p =  Producto.objects.filter(nombre__icontains = Categoria).all()
    
    product = categoria.productos.all()
    return render(request, 'productos/search.html',
    {
        'cata' : Categoria.objects.all(),
        'productos' : product,
        'categoria' : categoria.nombre,
        'titulo_seccion' : 'Productos de la categoria',
        'sin_productos' : 'No hay producto de la categoria ' + categoria.sigla
    })

       
                 
            


def delete_p(request,id):
    try:
        producto = get_object_or_404(Producto,id = id)
        producto.delete()
        return redirect(to='padre')
    except ValueError as i:
        print(i)
# Create your views here.
