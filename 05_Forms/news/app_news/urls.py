from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView, NewsFormView, NewsEditFormView, ChahgeListView

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("news_list", NewsListView.as_view(), name="news_list"),
    path("news_list/change_news_list", ChahgeListView.as_view(), name="change_news_list"),
    path("news_list/<int:pk>", NewsDetailView.as_view(), name="news-detail"),
    path("news_list/edit", NewsFormView.as_view()),
    path("news_list/<int:profile_id>/change", NewsEditFormView.as_view()),
]
