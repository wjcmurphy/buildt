from django.urls import path

from . import views

app_name = "vendors"

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:vendor_id>', views.detail, name='detail'),
]