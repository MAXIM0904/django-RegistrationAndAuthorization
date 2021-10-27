from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list(requset, *args, **kwargs):
    return render(requset, 'advertisement/advertisement_list.html', {})

def skill_1C(requset, *args, **kwargs):
    return render(requset, 'advertisement/skill_1C.html', {})

def skill_data_scientist(requset, *args, **kwargs):
    return render(requset, 'advertisement/skill_data_scientist.html', {})

def skill_graphic(requset, *args, **kwargs):
    return render(requset, 'advertisement/skill_graphic.html', {})

def skill_java(requset, *args, **kwargs):
    return render(requset, 'advertisement/skill_java.html', {})

def skill_python(requset, *args, **kwargs):
    return render(requset, 'advertisement/skill_python.html', {})