from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView



urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("advertisements", AdvertisementListView.as_view(), name="advertisements"),
    path("advertisements/<int:pk>/", AdvertisementDetailView.as_view(), name='advertisement-detail'),
]
