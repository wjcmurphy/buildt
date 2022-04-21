from django.urls import path, include
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.index, name='index'),
    path('about', views.about, name='about'),
    path('how', views.how, name='how'),
    path('contact', views.contact, name='contact')
]    