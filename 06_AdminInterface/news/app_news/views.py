from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from .models import News


def list_news(requset, *args, **kwargs):
    return render(requset, 'news/list_news.html', {})


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView, FormMixin):
    model = News
    template_name = 'news/news_detail.html'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("news_detail", kwargs={"pk": self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user_form_news = form.save(commit=False)
        user_form_news.id_news = self.get_object()
        user_form_news.author = self.request.user
        user_form_news.save()
        return super().form_valid(form)


class NewsCreateView(CreateView):
    model = News
    template_name = 'news/new_news.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('list_news')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/change.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('list_news')
