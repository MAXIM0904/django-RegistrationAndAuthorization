from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    name = models.CharField(max_length=100, verbose_name="Заголовок новости")
    text_news = models.TextField(verbose_name="Текст новости")
    update_news = models.DateTimeField(auto_now=True)
    created_news = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey("Status", default=None, null=True, on_delete=models.CASCADE,
                               verbose_name="Статус новости")

    class Meta:
        ordering = ["-created_news"]

    def __str__(self):
        return self.name


class Status(models.Model):
    status_news = models.CharField(max_length=50, verbose_name="Статус новости")

    def __str__(self):
        return self.status_news


class Comment(models.Model):
    id_news = models.ForeignKey("News", null=True, default="", on_delete=models.CASCADE, related_name='comments_news')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True,
                               default="")
    name = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Имя комментатора")
    text_comment = models.TextField(verbose_name="Текст комментария")
    created_comment = models.DateTimeField(auto_now_add=True, verbose_name="Дата комментария")


    class Meta:
        ordering = ["-created_comment"]

    def __str__(self):
        return self.text_comment
