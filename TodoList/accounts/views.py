from django.shortcuts import render
from .models import User
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(
        request,
        'accountform.html',
        {
            
        }
    )
    
@csrf_exempt
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return render(request, 'login.html')
        return render(request, 'accountform.html')
    
    return render(request, 'accountform.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/todo/')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})
    elif request.method == "GET":
        return render(request,'login.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/accounts/login/')
    return redirect('/todo/')