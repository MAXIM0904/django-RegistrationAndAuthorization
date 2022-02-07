from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, CommentListView, CommentDetailView
from .views import AnotherLoginView, AnotherLogoutView


urlpatterns = [
    path('', AnotherLoginView.as_view(), name='list_news'),
    path('news/news_list', NewsListView.as_view(), name='news_news_list'),
    path('news_list/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/new_news', NewsCreateView.as_view(), name='news_create'),
    path('change/<int:pk>', NewsUpdateView.as_view(), name='change'),
    path('comment_list', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('news/list_news', views.list_news, name='home_page'),
    path('news/login_page', views.aut_str, name='login_page'),
    path('news/another_logout', AnotherLogoutView.as_view(), name='another_logout'),
]
