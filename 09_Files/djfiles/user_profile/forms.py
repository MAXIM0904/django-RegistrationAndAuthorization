from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField, CharField
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


# class RegistrationForm(ModelForm):
#     user_name = CharField()
#     password = CharField(widget=PasswordInput)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class ProfileForms(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('field_about_yourself', 'avatar_user_img',)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
