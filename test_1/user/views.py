from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView

from .forms import CategoriesForm
from .models import Info, Categories


def home(request):
    return render(request,'home.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')

def profile(request):
    projects = Info.objects.all()
    projects_1 = Categories.objects.order_by('id')
    context = {
        'projects': projects,
        'projects_1': projects_1
    }
    return render(request, 'profile.html', context)

def create(request):
    error = ''
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error = 'Форма была не верной'
    form = CategoriesForm
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'create.html', context)

class Delete(DetailView):
    model = Categories
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
