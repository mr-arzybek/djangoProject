from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world_view, name='hello'),
    path('books/', views.book_view, name='books'),

]