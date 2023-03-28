from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models, forms


# не полная информация об автомобиле
def car_list_view(request):
    car_object = models.CarShop.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


# Полная информация об автомобиле по id
def car_detail_view(request, id):
    car_detail = get_object_or_404(models.CarShop, id=id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})


# Добавлние автомобиля через формы
def create_car_view(request):
    method = request.method
    if method == "POST":
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно добавлен в Базу Данных")
    else:
        form = forms.CarForm()
    return render(request, "create_car.html", {'form': form})


#Удаление автомобиля из базы
def delete_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    car_object.delete()
    return HttpResponse('Телефон удален из Базы данных')


#Редактирование автомобиля
def update_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно обновлены')
    else:
        form = forms.CarForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'update_car.html', context)


#Добавление отзыва к автомобилю
def reviews_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.ReviewsForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Отзыв успешно добавлен')
    else:
        form = forms.ReviewsForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'car_reviews.html', context)
