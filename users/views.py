from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from users.forms import AccountRegisterForm, UserUpdateForm
from users.models import Profile


# Create your views here.


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = "Your user account has been created!"

    def form_valid(self, form):
        user = form.save(commit=False)
        user_type = form.cleaned_data['user_types']
        if user_type == 'is_employee':
            user.is_employee = True
        elif user_type == 'is_employer':
            user.is_employer = True

        user.save()

        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/login.html'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    success_message = "You updated your profile !"
    template_name = 'users/update.html'
    form_class = UserUpdateForm