from django import forms
from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarShop
        fields = "__all__"


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = models.CarShop
        fields = ["reviews"]