from django.db import models


class News(models.Model):
    name_news = models.CharField(max_length=150,  verbose_name="Название статьи")
    content_news = models.TextField(verbose_name="Текст новости")
    update_news = models.DateTimeField(auto_now=True)
    created_news = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    author_news = models.ForeignKey("Author_news", default=None, null=True, on_delete=models.CASCADE,
                                    verbose_name="Автор новости")
    status = models.ForeignKey("Status_news", default=None, null=True, on_delete=models.CASCADE,
                               verbose_name="Статус новости")

    def __str__(self):
        return self.name_news


class Author_news(models.Model):
    name = models.CharField(max_length=1500, verbose_name="Имя автора")
    publication = models.CharField(max_length=2500, null=True, verbose_name="Редакция")

    def __str__(self):
        return self.name


class Status_news(models.Model):
    status_news = models.CharField(max_length=500, null=True, verbose_name="Статус новости")

    def __str__(self):
        return self.status_news
