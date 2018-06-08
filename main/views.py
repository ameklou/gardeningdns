from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from . forms import LoginForm
from dnsimple import DNSimple
# Create your views here.


token="tgOrJJxqkGfu3m01Mv0ssUo4S0MCpmkc"
email="geekrum@gmail.com"
password="#open@bunshin"
dns=DNSimple(email,password)
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
    #dns=DNSimple()
    print(dns.check('simpleklou.com'))
    return render(request,'main/dashboard.html')
