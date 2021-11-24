# Generated by Django 2.2 on 2021-11-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_auto_20211115_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=1500, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name_author',
            field=models.CharField(max_length=1500, verbose_name='Имя продавца'),
        ),
        migrations.AlterField(
            model_name='author',
            name='telephone',
            field=models.IntegerField(default=0, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование категории'),
        ),
    ]
