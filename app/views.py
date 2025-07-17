from django.shortcuts import render
from .models import Car, Category


def show_display(request):
    cars = Car.objects.all()
    return render(request=request, template_name='app/index.html', context={'cars': cars})

def car_info(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request=request, template_name='app/car_info.html', context={'car': car})



