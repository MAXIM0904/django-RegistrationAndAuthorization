from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home_page.as_view()),
    path('advertisement', views.Advertisement.as_view()),
    path('contacts', views.Contacts.as_view()),
    path('аbout', views.About.as_view()),
]
