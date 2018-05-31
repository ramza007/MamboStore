from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
#------------Home Page-----------#
@login_required(login_url='/accounts/login/')
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