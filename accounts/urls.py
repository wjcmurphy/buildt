from django.urls import path, include
from accounts.views import profile, signup
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"

urlpatterns = [    
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup, name="signup"),
    path("", include("django.contrib.auth.urls")),
]