from django.urls import path, re_path
from . import views
from .views import RegistrationLogOutView, RegistrationLoginView, UserListView, UserUpdateView

urlpatterns = [
    path('', RegistrationLoginView.as_view(), name='registration'),
    path('registration_logout', RegistrationLogOutView.as_view(), name='registration_logout'),
    path('signup', views.signup_view, name='signup'),
    path('ok_login', views.ok_login, name='ok_login'),
    path('registration_logout', views.registration_logout, name='registration_logout'),
    path('profile_list', UserListView.as_view(), name='profile_list'),
    path('update_user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    # re_path(r'update_user/\d+', views.update_user, name='update_user'),
]
