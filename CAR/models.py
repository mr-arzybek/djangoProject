from django.db import models


class CarShop(models.Model):
    CAR_TYPE = (
        ('Для молодых людей', "Для молодых людей"),
        ("Для работы", "Для работы"),
        ("Для большой семьи", "Для большой семье"),
        ("Для путешествий", "Для путешествий"),
        ("Для женщин", "Для женщин"),
        ("Для успешных", "Для успешных")
    )
    title = models.CharField("Название модели", max_length=100)
    description = models.TextField("Описание автомобиля")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    specifications = models.TextField("Характеристики", null=True)
    model_year = models.TextField("Модельный год", null=True)
    manufacturing_country = models.TextField("Страна изготовитель", null=True)
    reviews = models.TextField('Отзывы', blank=True, null=True)

    def __str__(self):
        return self.title
