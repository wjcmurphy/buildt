from django.urls import path, include
from . import views

app_name = 'resources'

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:resource_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit')
]    