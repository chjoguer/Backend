from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

# Create your views here.

def content(request):
    return render(request, 'views/contenido.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #Con esto crean los tipos de usarios mientras tanto para que vatan probando los diferentes tipos de usuarios
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

