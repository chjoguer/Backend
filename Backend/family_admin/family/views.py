from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def content(request):
    return render(request, 'views/contenido.html')

def view_eliminar_galeria(request):
    imagenes = Imagenes_galeria.objects.filter(id_galeria=1)#solo hay una galeria
    categorias = Categoria_Tema.objects.all()

    print(imagenes)
    return render(request, 'views/galeria/eliminar_galeria.html',{'imagenes':imagenes})

def eliminar_galeria(request,pk):
    imagenes = Imagenes_galeria.objects.filter(id_galeria=1) #solo hay una galeria
    image = Imagenes_galeria.objects.get(id=pk)   #solo hay una galeria
    image.delete()
    return render(request, 'views/galeria/eliminar_galeria.html',{'imagenes':imagenes})

def vista_buzon_entrada(request):
    return render(request, 'notificaciones/buzon_entrada.html')



def vista_registrar_tema(request):
    categorias = Categoria_Tema.objects.all()
    if(request.method == 'POST'):
        try:
            #Esteado enum 1:Aprobado, 2:Pendiente
            cate_tema = Categoria_Tema.objects.get(nombre_categoria=request.POST['categoria'])
            tema = Tema(estado=request.POST['estado'],
                        titulo=request.POST['titulo'],
                        tema_categoria=cate_tema,
                        descripcion=request.POST['descripcion'],
                        )
            if request.POST['fecha'] != '' :
                tema.fecha=request.POST['fecha']   
            tema.save()
                        
            #Esta podria ser la imagen que se muestra en el index del portal web
            imagen_tema_1 = Imagenes_Tema(id_tema=tema)
            imagen_tema_1.image = request.FILES['imagen1']
            imagen_tema_1.save()
            #Esta podria ser la imagen que se muestra una vez que le de click en el tema
            imagen_tema_2 = Imagenes_Tema(id_tema=tema)
            imagen_tema_2.image = request.FILES['imagen2']
            imagen_tema_2.save()

            #Video: Este se muestra una vez que entre en el tema
            vide_tema = Videos_Tema(id_tema=tema)
            vide_tema.video = request.FILES['video']
            vide_tema.save()


            #Que suba audio podria ser opcional (Casi a nadie le gusta estar oyendo audio de internet)
            messages.add_message(request, messages.SUCCESS, 'Tema guardado exitosamente.')
        except Exception as e :
            print("Errors -> ", e)
            messages.add_message(request,messages.ERROR,'Error al guardar el tema.')

        return redirect('registrar_tema') #registrar_tema es la version corta de views/registros/registrar_tema.html

    return render(request, 'views/registros/registrar_tema.html',{'categorias':categorias,"estado":Tema.Estado})


def view_modificar_tema(request):
    All_temas = Tema.objects.all()
    categorias = Categoria_Tema.objects.all()
    return render(request, 'views/modificaciones/modificar_tema.html',{'temas':All_temas,'categorias':categorias,"estado":Tema.Estado})
@csrf_exempt
def modificar_tema(request,pk):
    All_temas = Tema.objects.all()
    categorias = Categoria_Tema.objects.all()
    try:
        tema = Tema.objects.get(id_tema=pk)
        if request.method == 'POST':
            tema.titulo= request.POST['titulo']
            tema.fecha=request.POST['fecha']
            tema.descripcion=request.POST['descripcion']
            tema.estado=request.POST['estado']
            tema.save()     

            imagenes_tema = Imagenes_Tema.objects.filter(id_tema=pk)[0]
            imagenes_tema.image=request.FILES['imagen1']
            imagenes_tema.save()
            imagenes_tema2 = Imagenes_Tema.objects.filter(id_tema=pk)[1]
            imagenes_tema2.image=request.FILES['imagen1']
            imagenes_tema2.save()
            messages.add_message(request, messages.SUCCESS, 'Modificacion exitosa.')
            return render(request, 'views/modificaciones/modificar_tema.html',{'temas':All_temas,'categorias':categorias,"estado":Tema.Estado,'tema':tema})
    except Exception as e:
        print("Error ->", e.args)
        messages.add_message(request, messages.ERROR, 'No se pudo realizar la modificacion.')
    return render(request, 'views/modificaciones/modificar_tema.html',{'temas':All_temas,'categorias':categorias,"estado":Tema.Estado,'tema':tema})


def view_eliminar_tema(request):
    All_temas = Tema.objects.all()
    categorias = Categoria_Tema.objects.all()
    return render(request, 'views/eliminacion/eliminar_tema.html',{'temas':All_temas,'categorias':categorias,"estado":Tema.Estado})

def eliminar_tema(request,pk):
    try:
        print(pk)
        tema = Tema.objects.get(id_tema=pk)
        imagenes = Imagenes_Tema.objects.filter(id_tema=tema.id_tema)
        for imagen in imagenes:
            imagenes.delete()
        videos = Videos_Tema.objects.filter(id_tema=tema)
        videos.delete()
        tema.delete()
        print(imagenes)
        messages.add_message(request, messages.SUCCESS, 'Tema eliminado exitosamente.')
    except Exception as e:
        print(e)
        messages.add_message(request,messages.ERROR,'Error al eliminar el tema.')

    categorias = Categoria_Tema.objects.all()
    return redirect('eliminar_tema')


def view_galeria(request):
    return render(request, 'views/galeria/view_galeria.html')



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #Con esto crean los tipos de usarios mientras tanto para que vayan probando los diferentes tipos de usuarios
        #new = UserProfile.objects.create_user('john', 'lennon@thebeatles.com', '23198')
        #new.tipo = "A"
        #new.save()
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                #redirect('index')
                try:
                    usuario = UserProfile.objects.get(username=username)
                    print(usuario.username)
                    pass
                except expression as identifier:
                    pass
                if usuario.tipo == "E": #Editor
                    return redirect('index')
                elif usuario.tipo == "A": #Administrador
                    return redirect('index')
                elif usuario.tipo == "C": #Consejero
                    return redirect('index')
            else:
                # Return a 'disabled account' error message
                return render(request, 'views/login.html', {})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'views/login.html', {})
    else:
        return render(request, 'views/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')
    # Redirect to a success page.
    # try:
    #     del request.session['username']
    # except:
    #  pass
    # return render(request, 'app_foldername/login.html', {})

