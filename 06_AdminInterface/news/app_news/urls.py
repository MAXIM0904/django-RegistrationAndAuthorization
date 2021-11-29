from django.contrib import admin
from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('', views.list_news, name='list_news'),
    path('news/news_list', NewsListView.as_view(), name='news_news_list'),
    path('news_list/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/new_news', NewsCreateView.as_view(), name='news_create'),
    path('change/<int:pk>', NewsUpdateView.as_view(), name='change')
]
