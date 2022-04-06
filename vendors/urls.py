from django.urls import path, include

from . import views

app_name = "vendors"

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:vendor_id>', views.detail, name='detail'),
    path('<int:vendor_id>/resources/', include('resources.urls', namespace='resources'))
]