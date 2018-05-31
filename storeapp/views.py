from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import  Image, Profile
# , Comment, Like, Follow,Profile,
from .forms import ProfileForm
# ImagePostForm, CommentForm, ProfileForm


# Create your views here.
#------------Home Page-----------#
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


#--------------Profile Function--------------#
@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Image.objects.filter(user=request.user.id).all()

    except:

        title = f'{current_user.username}'

        pics = Image.objects.filter(user=request.user.id).all()

        info = Profile.objects.filter(user=7)

    return render(request, 'my-profile.html', {"title": title, "current_user": current_user, "info": info, "pics": pics})

@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    profiles = Profile.objects.filter(user=current_user).count()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            if profiles == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
            else:
                record = Profile.objects.filter(user=current_user)
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
    else:
        form = ProfileForm()
    return render(request, 'update-profile.html', {"form": form})

#---------------MamboStore Functions-------------#
@login_required(login_url='/accounts/login/')
def store(request):
    return render(request, 'store.html')

