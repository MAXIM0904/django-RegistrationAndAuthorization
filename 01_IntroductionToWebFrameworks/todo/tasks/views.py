from django.http import HttpResponse

from django.views import View
from random import sample

class ToDoView(View):


    def get(self, request, *args, **kwargs):
        list_todo = sample(('<li>Установить python</li>',
                            '<li>Установить django</li>',
                            '<li>Запустить сервер</li>',
                            '<li>Найти views.py</li>',
                            '<li>Написать здесь задачи</li>',
                            '<li>Сдать домашнее задание</li>',
                            '<li>Добавить random sample</li>',
                            '<li>Порадоваться результату</li>'), 5)

        return HttpResponse('<ul>'
                            f"{''.join(list_todo)}"
                            '</ul>')
