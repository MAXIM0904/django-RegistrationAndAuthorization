from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import SignupForm, ProfileForm, UserEditForm
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
                users = new_user,
                phone_number= phone_number,
                city= city
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'news/ok_login.html', {'user_form': new_user})
    else:
        user_form = SignupForm()
        return render(request, 'news/signup.html', {'user_form': user_form})


class UserListView(PermissionRequiredMixin, ListView):
    """ класс просмотра списка пользователей """
    model = User
    template_name = 'news/profile_list.html'
    permission_required = 'request.user.users.verification_flag'


@permission_required('request.user.users.superuser_flag')
def update_user(request):
    """ функция данных пользователя """
    id_profile_user = request.META['PATH_INFO'].split('/')[-1]
    profile = Profile.objects.get(users_id=id_profile_user)
    user_profile = User.objects.get(id=profile.users_id)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user_profile)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            if profile_form.cleaned_data.get('superuser_flag'):
                    profile.superuser_flag = True
                    profile.verification_flag = True
            user_profile.save()
            profile.save()
        return redirect('profile_list')

    else:
        user_form = UserEditForm(instance=user_profile)
        profile_form = ProfileForm(instance=profile)
        user_verification_flag = Profile.objects.get(users_id=request.user.id)
        user_superuser_flag = Profile.objects.get(users_id=request.user.id).superuser_flag

        return render(request, 'news/update_user.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_verification_flag': user_verification_flag,
            'user_superuser_flag': user_superuser_flag,
        })
