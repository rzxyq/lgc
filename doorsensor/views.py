from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Walkin, Walkout

def home(request):
    context = {
        
    }
    return render(request, 'home.html', context)

def sensor(request):
    data = request.GET.get('data')
    if data=='in':
        new_walkin = Walkin()
        new_walkin.save()
    elif data=='out':
        new_walkout = Walkout()
        new_walkout.save()

    num_walkin = Walkin.objects.all().count()
    num_walkout = Walkout.objects.all().count()

    context = {
        "num_walkin": num_walkin,
        "num_walkout": num_walkout,
    }
    return render(request, 'sensor.html', context)

def reset(request):
    Walkout.objects.all().delete()
    Walkin.objects.all().delete()

    context = {
        
    }
    return redirect('/sensor')