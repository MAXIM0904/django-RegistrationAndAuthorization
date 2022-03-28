from django.urls import path
from .views import RegisterLoginView, RegisterLoginOutView, UpdateUserProfile, ProfileDetailView
from . import views

app_name = 'profile'

urlpatterns = [
    path('login_user', RegisterLoginView.as_view(), name='login_user'),
    path('logout_user', RegisterLoginOutView.as_view(), name='logout_user'),
    # path('ok_login', views.ok_login, name='ok_login'),
    path('signup', views.signup, name='signup'),
    path('update_user_profile', UpdateUserProfile.as_view(), name='update_user_profile'),
    path('profile_detail/<int:pk>', ProfileDetailView.as_view(), name='profile_detail'),
]
