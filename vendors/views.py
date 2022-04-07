from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor
from .forms import VendorForm

# Site index, this should change
def index(request):    
    return render(request, 'vendors/index.html')

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, "vendors/detail.html", {'vendor': vendor}) 

def list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/list.html', {'vendors': vendors})

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

