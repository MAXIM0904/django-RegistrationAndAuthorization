# Generated by Django 2.2 on 2021-11-22 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500, verbose_name='Имя автора')),
                ('publication', models.CharField(max_length=2500, null=True, verbose_name='Редакция')),
            ],
        ),
        migrations.CreateModel(
            name='Status_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_news', models.CharField(max_length=500, null=True, verbose_name='Статус объявления')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_news', models.CharField(max_length=150, verbose_name='Название статьи')),
                ('content_news', models.TextField(verbose_name='Текст новости')),
                ('update_news', models.DateTimeField(auto_now=True)),
                ('created_news', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('author_news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.Author_news')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.Status_news')),
            ],
        ),
    ]