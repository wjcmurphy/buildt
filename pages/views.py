from django.shortcuts import render

# Create your views here.

def index(request):    
    return render(request, 'pages/index.html')

def about(request):
    return render(request, "pages/about.html") 

def how(request):
    return render(request, 'pages/how.html')

def contact(request):
    return render(request, 'pages/contact.html')