from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    return render(request, 'home.html')




def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'signin.html')
    
def signout(request):
    logout(request)
    return redirect('home')