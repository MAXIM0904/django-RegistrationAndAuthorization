from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
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


class UserListView(ListView):
    """ класс просмотра списка пользователей """
    model = User
    template_name = 'news/profile_list.html'


def update_user(request):
    """ функция данных пользователя """
    id_profile_user = request.META['PATH_INFO'].split('/')[-1]
    profile = Profile.objects.get(users_id=id_profile_user)
    user_profile = User.objects.get(id=profile.users_id)

    if request.method == 'POST':
        profile.superuser_flag = False
        profile.superuser_flag = False
        for i_request in request.POST:
            if i_request == 'username':
                user_profile.username = request.POST['username']

            if i_request == 'last_name':
                user_profile.last_name = request.POST['last_name']

            if i_request == 'city':
                profile.city = request.POST['city']

            if i_request == 'phone_number':
                profile.phone_number = request.POST['phone_number']

            if i_request == 'verification_flag':
                profile.verification_flag = True

            if i_request == 'superuser_flag':
                profile.superuser_flag = True

        user_profile.save()
        profile.save()
        return redirect('profile_list')

    else:
        user_form = SignupForm(instance=user_profile)
        profile_form = ProfileForm(instance=profile)
        print(Profile.objects.get(users_id=request.user.id))
        user_verification_flag = Profile.objects.get(users_id=request.user.id)
        user_superuser_flag = Profile.objects.get(users_id=request.user.id).superuser_flag

        return render(request, 'news/update_user.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_verification_flag': user_verification_flag,
            'user_superuser_flag': user_superuser_flag,
        })
