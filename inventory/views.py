from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop, Desktop, Mobile
from .forms import DesktopForm, LaptopForm, MobileForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def display_laptops(request):
    header = 'Laptop stock'
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': header
    }
    return render(request, 'index.html', context)


def display_desktops(request):
    header = 'Desktops stock'
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': header
    }
    return render(request, 'index.html', context)


def display_mobiles(request):
    header = 'Mobiles stock'
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': header
    }
    return render(request, 'index.html', context)


def add_device(request, cls):
    if request.method == 'POST':
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


# edit
'''def edit_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)

    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = LaptopForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})'''


def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def edit_laptop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)


def edit_desktop(request, pk):
    return edit_device(request, pk, Desktop, DesktopForm)


def edit_mobile(request, pk):
    return edit_device(request, pk, Mobile, MobileForm)


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def delete_mobile(request, pk):
    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
