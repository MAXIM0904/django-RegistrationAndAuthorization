from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
import os.path

class Home_page(View):

    def get(self, request):
        advertisements = [
            # self.counter,
            'Выбор категории из списка',
            'Выбор региона из списка',
        ]

        text_fild = f'input type = "text" name = "userName" ' \
                    f'placeholder = Tекстовое_поле_для_ввода_названия_объявления size = 50'

        button = 'button type=button></button'
        button_name = 'Нажать'
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                          'title': 'Главная страница',
                                                                          'text_fild': text_fild,
                                                                          'button': button,
                                                                          'button_name': button_name})



class Advertisement(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if os.path.exists('count.txt'):
            with open("count.txt", "r") as file:
                self.counter = int(file.read())
        else:
            self.counter = 0
            with open("count.txt", "w") as file:
                file.write(f'{self.counter}')


    def count(self):
        self.counter += 1
        with open("count.txt", "w") as file:
            file.write(f'{self.counter}')
        return self.counter


    def get(self, request):
        self.counter = self.count()
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
                                                                          'counter': f'{self.counter} GET запрос.'})

    def post(self, request):
        message = "Запрос на создание новой записи успешно выполнен"
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': message})


class Contacts(TemplateView):

    template_name = 'advertisements/advertisement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = ['Mосква; +79122345467; dvdvdvdv90@mail.ru',
                           'Ярославль; +79405679809; sinom@mail.ru',
                           'Омск; +79789879888; uioihjui@mail.ru'
                           ]
        context['title'] = 'Контактные данные'

        return context

class About(TemplateView):

    template_name = 'advertisements/advertisement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = ['IKEA -  Сеть торговых центров компании насчитывала 231 магазин в 24 странах мира '
                                     '(на конец 2008 года), по большей части в Европе; 273 магазина в 25 странах мира '
                                     '(май 2010); с учётом магазинов, открытых на основе франчайзинга, сеть состоит из '
                                     '325 магазинов в 41 стране мира (2013).']
        context['title'] = 'О компании'
        return context
