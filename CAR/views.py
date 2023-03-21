from django.shortcuts import render, get_object_or_404

from . import models


# не полная информация об автомобиле
def car_list_view(request):
    car_object = models.CarShop.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


# Полная информация об автомобиле по id
def car_detail_view(request, id):
    car_detail = get_object_or_404(models.CarShop, id=id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})
