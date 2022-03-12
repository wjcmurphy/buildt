from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm

# Create your views here.
def index(request):    
    return render(request, 'vendors/index.html')

def create(request):
    form = VendorForm()

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')

    context = {
        'form': form,
    }
    return render(request, 'vendors/create.html', context)

def detail(request):
    return render(request, "vendors/detail.html") 