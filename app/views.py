from email.mime import image
from unicodedata import category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Category


def show_display(request):
    cars = Car.objects.all()
    return render(request=request, template_name='app/index.html', context={'cars': cars})

def car_info(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request=request, template_name='app/car_info.html', context={'car': car})

def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        year = request.POST.get('year')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')  # важно

        category = Category.objects.get(id=category_id)

        Car.objects.create(
            name=name,
            model=model,
            price=price,
            year=year,
            description=description,
            category=category,
            image=image
        )

        return redirect('show_display')  # это имя URL'а, не шаблона

        # сюда попадаем, если GET-запрос
    categories = Category.objects.all()
    return render(request, 'app/add_car.html', {'categories': categories})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('show_display')

def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.name = request.POST.get('name')
        car.model = request.POST.get('model')
        car.price = request.POST.get('price')
        car.year = request.POST.get('year')
        car.description = request.POST.get('description')
        category_id = request.POST.get('category')
        if category_id:
            car.category = Category.objects.get(id=category_id)

        image = request.FILES.get('image')
        if image:
            car.image = image

        car.save()
        return redirect('show_display')
    categories = Category.objects.all()
    return render(request, 'app/update_car.html', {'car': car, 'categories': categories})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно создали аккаунт')
            return redirect('show_display')
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{errors}')
    form = UserCreationForm()
    return render(request, 'app/user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('show_display')
        messages.error(request, 'Неправильный логин или пароль')
    return render(request, 'app/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта')
    return redirect('show_display')

