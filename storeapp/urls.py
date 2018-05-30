"""

App routes and paths

"""
from django.conf.urls import url
from . import views

#--------------App routes--------------#
urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^profile/', views.profile, name = 'profile'),
    url(r'^stores/', views.store, name= 'stores')
]