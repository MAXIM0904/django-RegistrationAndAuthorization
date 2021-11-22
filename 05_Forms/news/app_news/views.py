from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View
from .models import News
from .forms import NewsForm


def home_page(requset):
    return render(requset, 'news/news_home_page.html', {})


class NewsListView(generic.ListView):
    model = News
    template_name = "news/news_list.html"




class NewsDetailView(generic.DetailView):
    model = News
    template_name = "news/news_detail.html"

    def get(self, reguest, *args, **kwargs):
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