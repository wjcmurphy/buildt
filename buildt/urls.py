"""buildt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from importlib import resources
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required

import vendors.views, resources.views

app_name = 'buildt'

urlpatterns = [
    path('', vendors.views.index, name="index"),
    path('vendors/', include('vendors.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('resources/', include('resources.urls')),
    path('search/', resources.views.search, name="search"),
    path('search_results/', resources.views.search_results, name="search_results")


    # path('accounts/profile/', name='profile'),
]
