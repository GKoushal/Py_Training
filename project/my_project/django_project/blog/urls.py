from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='blog-home'),
    #path("", , name='blog-about'),
]


#http://localhost:8000/blog/home