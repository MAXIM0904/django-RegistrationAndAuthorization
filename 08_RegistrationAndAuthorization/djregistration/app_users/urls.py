from . import views
from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

app_name = 'app_users'

urlpatterns = [
    path('home_page', views.home_page, name='home_page'),
    path('news_list', NewsListView.as_view(), name='news_list'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('create_news', NewsCreateView.as_view(), name='create_news'),
    path('update_news/<int:pk>', NewsUpdateView.as_view(), name='update_news'),
]