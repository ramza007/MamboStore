"""

App routes and paths

"""
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

#--------------App routes--------------#
urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/', views.profile, name = 'profile'),
    url(r'^stores/', views.store, name= 'stores'),
    url(r'^update/profile/', views.create_profile, name="createProfile"),
    url(r'^post/', views.new_post, name='postImage'),
    url(r'^manage/(\d+)', views.manage_image, name='manageImage'),
    url(r'^other/profile/(\d+)', views.other_profile, name='otherProfile'),
    url(r'^single/image/(\d+)', views.single_image, name='singleImage'),
    # url(r'^no-profile/', views.no_profile, name = 'noprofile'),


    #--------------Functions-------------#
    url(r'^delete/post/(\d+)', views.delete_post, name="removePost"),
    url(r'^like/(\d+)', views.like, name="like"),
    url(r'^comment/(\d+)', views.new_comment, name='Comment'),
    url(r'^unfollow/(\d+)', views.unfollow, name="unfollow"),
    url(r'^follow/(\d+)', views.follow, name="follow"),
    url(r'^search/', views.search_results, name='search_results'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)