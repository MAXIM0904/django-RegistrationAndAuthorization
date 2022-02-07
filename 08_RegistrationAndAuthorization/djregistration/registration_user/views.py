from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .forms import SignupForm, ProfileForm
from .models import Profile



class RegistrationLoginView(LoginView):
    """ класс регистрации пользователя """
    template_name = "news/registration.html"


class RegistrationLogOutView(LogoutView):
    """ класс регистрации пользователя """
    template_name = "news/registration_logout.html"


def ok_login(request, *args, **kwargs):
    """ функция успешная регистрация пользователя """
    return render(request, 'news/ok_login.html')


def registration_logout(request, *args, **kwargs):
    """ функция выхода пользователя """
    return render(request, 'news/registration_logout.html')


def signup_view(request):
    """ класс для регистрации пользователя """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            Profile.objects.create(
                user = new_user,
                phone_number=phone_number,
                city=city
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'news/ok_login.html', {'user_form': new_user})
    else:
        user_form = SignupForm()
        return render(request, 'news/signup.html', {'user_form': user_form})



class UserListView(ListView):
    """ класс просмотра списка пользователей """
    model = Profile
    template_name = 'news/profile_list.html'


class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'news/update_user.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        self.success_url = '/profile_list'
        return str(self.success_url)


# def update_user(request):
#     """ класс своих данных пользователя """
#     if request.POST == 'POST':
#         pass
#     else:
#         user_form = SignupForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user)
#         return render(request, 'news/update_user.html', {'user_form': user_form, 'profile_form': profile_form})
#
#         #
#         # self.success_url = '/profile_list'
#         # return str(self.success_url)