from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource, Vendor
from .forms import ResourceForm

# Create your views here.

def index(request):
    return render(request, 'resources/index.html')

def detail(request, resource_id):
    context = {resource_id: resource_id}
    return render(request, 'resources/detail.html', context)

def create(request, vendor_id):
    form = ResourceForm()

    if request.method == 'POST':
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.instance.vendor = vendor
            form.save()
            return redirect('../')

    context = {
        'form': form,
    }
    return render(request, 'resources/create.html', context)

def edit(request):
    return render(request, 'resources/edit.html')