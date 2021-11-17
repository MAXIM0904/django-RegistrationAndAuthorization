from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView



urlpatterns = [
    # path("", views.home_page, name="home_page"),
    # path("advertisements", views.advertisements, name="advertisements"),
    path("", AdvertisementListView.as_view(), name="advertisement"),
    path("advertisements/<int:pk>/", AdvertisementDetailView.as_view(), name='advertisement-detail')
]
