from django.contrib import admin
from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, CommentListView, CommentDetailView

urlpatterns = [
    path('', views.list_news, name='list_news'),
    path('news/news_list', NewsListView.as_view(), name='news_news_list'),
    path('news_list/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/new_news', NewsCreateView.as_view(), name='news_create'),
    path('change/<int:pk>', NewsUpdateView.as_view(), name='change'),
    path('comment_list', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail')
]
