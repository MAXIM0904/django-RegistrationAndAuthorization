from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import FormMixin
from .models import News
from .forms import NewsForm, CommentForm


def home_page(requset):
    return render(requset, 'news/news_home_page.html', {})


class NewsListView(generic.ListView):
    model = News
    template_name = "news/news_list.html"


class ChahgeListView(generic.ListView):
    model = News
    template_name = "news/change_news_list.html"


class NewsDetailView(generic.DetailView, FormMixin):
    model = News
    template_name = "news/news_detail.html"
    form_class = CommentForm


    def get_success_url(self, **kwargs):
        return reverse_lazy("news-detail", kwargs={"pk": self.get_object().id})


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        contex = self.get_context_data(object=self.object)
        return self.render_to_response(contex)


class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, "news/edit.html", context={"news_form": news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect("/")
        return render(request, "news/edit.html", context={"news_form": news_form})


class NewsEditFormView(View):
    def get(self, request, profile_id):
        user = News.objects.get(id=profile_id)
        news_form = NewsForm(instance=user)
        return render(request, "news/change.html", context={"news_form": news_form, "profile_id": profile_id})

    def post(self, request, profile_id):
        user = News.objects.get(id=profile_id)
        news_form = NewsForm(request.POST, instance=user)
        if news_form.is_valid():
            user.save()
            return HttpResponseRedirect("/")
        return render(request, "news/change.html", context={"news_form": news_form, "profile_id": profile_id})
