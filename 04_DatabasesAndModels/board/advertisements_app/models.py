from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name="Название объявления")
    description = models.TextField(default="", verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    price = models.FloatField(verbose_name="Цена", default=0)
    views_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    status_category = models.ForeignKey("Category", default=None, null=True, on_delete=models.CASCADE)
    status_author = models.ForeignKey("Author", default=None, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


class Author(models.Model):
    name_author = models.CharField(max_length=1500, verbose_name="Имя продавца")
    email = models.CharField(max_length=100)
    telephone = models.IntegerField(verbose_name="Номер телефона", default=0)

    def __str__(self):
        return self.name_author


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")

    def __str__(self):
        return self.name
