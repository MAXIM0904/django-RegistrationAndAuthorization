from django.db import models



class News(models.Model):
    hedline_news = models.CharField(max_length=100)
    text_news = models.TextField(verbose_name="Текст новости")
    update_news = models.DateTimeField(auto_now=True)
    created_news = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status_news', on_delete=models.CASCADE, verbose_name='Статус новости')


class Status_news(models.Model):
    str_status = models.CharField(max_length=50, verbose_name='Статус новости')


