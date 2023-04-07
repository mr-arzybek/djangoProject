from django.db import models
from django.contrib.auth.models import User

class Customuser(User):
    ADMIN = 1
    VIPVlient = 2
    CLIENT = 3
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (VIPVlient, 'VIPVlient'),
        (CLIENT, 'CLIENT')
    )

    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_TYPE = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    )
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField('Номер телефона', max_length=100)
    age = models.PositiveIntegerField('ваш возраст')
    user_type = models.IntegerField('Тип пользователя', choices=USER_TYPE)
    gender = models.IntegerField('Пол', choices=GENDER_TYPE)