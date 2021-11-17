from django.shortcuts import render
from .models import Advertisement
from django.views.generic import ListView, DetailView


# def home_page(reguest, *args, **kwargs):
#     return render(reguest, "advertisements/home_page.html", {})
#

# def advertisements(reguest, *args, **kwargs):
#     advertisements = Advertisement.objects.all()
#     return render(reguest, "advertisements/advertisements.html", {"advertisements": advertisements})


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = "advertisements/advertisement_list.html"


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = "advertisements/advertisement_detail.html"

    def get(self, reguest, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        contex = self.get_context_data(object=self.object)
        return self.render_to_response(contex)
