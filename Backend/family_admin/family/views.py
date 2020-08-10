from django.shortcuts import render
from django.contrib.auth.models import User 

# Create your views here.
def index(request):
    return render(request, "views/prueba.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("index")
        else:
            return render(request, 'views/login.html', {})
    return render(request, 'views/login.html', {})