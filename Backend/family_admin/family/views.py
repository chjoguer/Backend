from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'views/prueba.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                #redirect('index')
                return render(request, 'views/index.html', {})
            else:
                # Return a 'disabled account' error message
                return render(request, 'views/login.html', {})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'views/login.html', {})
    else:
        return render(request, 'views/login.html', {})

def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return render(request, 'app_foldername/login.html', {})