from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, DetailView
from .forms import SignupForm, UserForm, ProfileForms
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class RegisterLoginView(LoginView):
    """ класс регистрации пользователя """
    template_name = "profile/login_user.html"


class RegisterLoginOutView(LogoutView):
    """ класс выхода из учетной записи пользователя"""
    template_name = "profile/logout_user.html"


def signup(request, *args, **kwargs):
    ''' Функция регистрации пользователя '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            UserProfile.objects.create(
                user_profile = new_user
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/update_user_profile')
        else:
            return render(request, 'profile/signup.html', {'user_form': form})
    else:
        user_form = SignupForm()
        return render(request, 'profile/signup.html', {'user_form': user_form})


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    ''' Редактирование профиля пользователя '''
    model = User
    form_class = UserForm
    second_form_class = ProfileForms
    template_name = 'profile/update_user_profile.html'

    def get(self, request, *args, **kwargs):
        self.object = request.user
        user_bd = User.objects.get(id=request.user.id)
        profile_bd = UserProfile.objects.get(user_profile_id=request.user.id)
        form_user = self.form_class(instance=user_bd)
        form_profile = self.second_form_class(instance=profile_bd)
        return self.render_to_response(self.get_context_data(object=self.object, user_form=form_user,
                                                             profile_form=form_profile))

    def post(self, request, *args, **kwargs):
        self.object = request.user
        user_bd = User.objects.get(id=request.user.id)
        profile_bd = UserProfile.objects.get(user_profile_id=request.user.id)
        user_form = self.form_class(request.POST, request.FILES, instance=user_bd)
        profile_form = self.second_form_class(request.POST, request.FILES, instance=profile_bd)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(f'/profile/profile_detail/{request.user.id}')
        else:
            return self.render_to_response(self.get_context_data(object=self.object, user_form=user_form,
                                                                 profile_form=profile_form))


class ProfileDetailView(LoginRequiredMixin, DetailView):
    ''' Класс возвращает информацию о пользователе '''
    model = UserProfile
    template_name = 'profile/profile_detail.html'
    form_class = UserForm
    second_form_class = ProfileForms

    def get(self, request, *args, **kwargs):
        self.object = request.user
        profile_bd = UserProfile.objects.get(user_profile_id=request.user.id)
        return self.render_to_response(self.get_context_data(object=self.object,
                                                             profile_form=profile_bd))
