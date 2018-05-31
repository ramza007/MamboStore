from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


#--------------Profile Function--------------#
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'my-profile.html')

#---------------MamboStore Functions-------------#
@login_required(login_url='/accounts/login/')
def store(request):
    return render(request, 'store.html')