from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from . models import News
from django.forms import HiddenInput

#функция главной страницы
def home_page(request, *args, **kwargs):
    print(request)
    return render(request, 'news/home_page.html', {})


#классы просмотра новостей
class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView, FormMixin):
    model = News
    template_name = 'news/news_detail.html'
    form_class_user = CommentForm

    def get_success_url(self, **kwargs):
        self.success_url = f'/app_users/news_detail/{self.get_object().id}'
        return str(self.success_url)


    def get_form(self, form_class=form_class_user):
        form = super().get_form(form_class)
        if self.request.user.is_authenticated:
            form.fields['name_commentator'].widget = HiddenInput()
        return form


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        user_form_news = form.save(commit=False)
        user_form_news.news_comment = self.get_object()
        if self.request.user.is_authenticated:
            user_form_news.name_commentator = self.request.user
        else:
            user_form_news.name_commentator = f"Аноним {self.request.POST['name_commentator']}"
        user_form_news.save()
        return super().form_valid(form)


# класс добавления новости
class NewsCreateView(CreateView):
    model = News
    template_name = 'news/create_news.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        self.success_url = '/app_users/create_news'
        return str(self.success_url)


# класс редактирования комментариев
class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update_news.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        self.success_url = '/app_users/news_list'
        return str(self.success_url)

