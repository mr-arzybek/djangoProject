from django.shortcuts import render
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from custom_users.form import CustomRegistrationForm


class Registration(CreateView):
    form_class = CustomRegistrationForm
    # form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'register.html'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()