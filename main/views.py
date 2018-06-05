from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from . forms import LoginForm
# Create your views here.




def index(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            if user.is_active:
                login(request, user)
                return render(request,"main/index.html")
            else:
                return HttpResponse('veillez activer votre compte')
        else:
            return HttpResponse("Vous n'avez pas de compte veillez vous inscrire")
    else:
        if request.user.is_authenticated():
            return HttpResponse("Vous avez un compte")
            #return redirect('dashboard')
        else:
            form= LoginForm()
            return render(request, 'main/index.html',{'form':form})


def dashboard(request):
    return render(request,'main/dashboard.html')
