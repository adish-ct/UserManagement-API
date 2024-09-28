from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserUpdationForm
from .models import CustomUser

# Create your views here.
def sample(request, *args, **kwargs):
    return HttpResponse('True')


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name ='signup.html'
    success_url = reverse_lazy('login')



class CustomLoginView(LoginView):
    template_name = 'login.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdationForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('signup')

    def get_object(self):
        return self.request.user


