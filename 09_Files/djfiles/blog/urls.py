from django.urls import path
from .views import RecordBlogListView, BlogCreateView, BlogDetailView, massive_blog_update



urlpatterns = [
    path('', RecordBlogListView.as_view(), name='record_list'),
    path('createview', BlogCreateView.as_view() , name='createview'),
    path('detailview/<int:pk>', BlogDetailView.as_view(), name='detailview'),
    path('massive_blog_update', massive_blog_update, name='massive_blog_update'),
]
