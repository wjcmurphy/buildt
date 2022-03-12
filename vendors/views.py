from django.shortcuts import render

# Create your views here.
def index(request):    
    return render(request, 'vendors/index.html')

def create(request):
    return render(request, "vendors/index.html")

def detail(request):
    return render(request, "vendors/detail.html") 