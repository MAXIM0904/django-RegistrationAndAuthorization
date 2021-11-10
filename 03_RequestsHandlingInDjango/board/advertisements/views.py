from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render


class Home_page(View):

    def get(self, request):
        advertisements = [
            'Выбор категории из списка',
            'Выбор региона из списка',
        ]

        return render(request, 'advertisements/home_page.html', {'advertisements': advertisements,
                                                                          'title': 'Главная страница'})


class Advertisement(View):
    counter = 0

    def get(self, request):
        Advertisement.counter += 1
        print(self.counter)

        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Услуги электрика',
            'Работа без выходных и отпуска'
        ]
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                          'title': 'Список объявлений',
                                                                          'counter': f'{Advertisement.counter} '
                                                                                     f'GET запрос.'})

    def post(self, request):
        Advertisement.counter += 1
        message = ["Запрос на создание новой записи успешно выполнен."]
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': message,
                                                                          'title': 'Список объявлений POST',
                                                                          'counter': f'{Advertisement.counter} '
                                                                                     f'POST запрос.'})


class Contacts(TemplateView):

    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = ['Mосква; +79122345467; dvdvdvdv90@mail.ru',
                           'Ярославль; +79405679809; sinom@mail.ru',
                           'Омск; +79789879888; uioihjui@mail.ru'
                           ]
        context['title'] = 'Контактные данные'

        return context

class About(TemplateView):

    template_name = 'advertisements/аbout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = ['IKEA -  Сеть торговых центров компании насчитывала 231 магазин в 24 странах мира '
                                     '(на конец 2008 года), по большей части в Европе; 273 магазина в 25 странах мира '
                                     '(май 2010); с учётом магазинов, открытых на основе франчайзинга, сеть состоит из '
                                     '325 магазинов в 41 стране мира (2013).']
        context['title'] = 'О компании'
        return context
