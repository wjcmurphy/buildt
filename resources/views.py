from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Resource, Vendor
from .forms import ResourceForm, BookingForm

# Create your views here.

def index(request):
    resources = Resource.objects.all()
    context = {'resources': resources}
    return render(request, 'resources/index.html', context)

def detail(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    context = {'resource': resource}
    return render(request, 'resources/detail.html', context)

def book(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    booking = BookingForm(request.POST)
    if booking.is_valid():
        booking.instance.resource = resource
        booking.save()
        return redirect('resources:detail', resource_id=resource.id)
    context = {
        'form': booking
    }
    return render(request, 'resources/detail.html', context)    

def create(request, vendor_id):
    form = ResourceForm()

    if request.method == 'POST':
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.instance.vendor = vendor
            form.save()
            return redirect('vendors:detail', vendor_id=vendor_id)

    context = {
        'form': form,
    }
    return render(request, 'resources/create.html', context)

def edit(request):
    return render(request, 'resources/edit.html')

def search(request):
   return render(request, "resources/search.html")  

def search_results(request):
    results = Resource.objects.filter(
        Q(first_name__contains=request.GET['q']) | 
        Q(last_name__contains=request.GET['q'] ) |
        Q(title__contains=request.GET['q'] ) 
    )
    return render(request, "resources/search_results.html", {'results': results})   