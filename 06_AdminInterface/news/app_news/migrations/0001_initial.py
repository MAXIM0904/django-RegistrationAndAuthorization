# Generated by Django 2.2 on 2021-11-29 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_news', models.CharField(max_length=50, verbose_name='Статус новости')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Заголовок новости')),
                ('text_news', models.TextField(verbose_name='Текст новости')),
                ('update_news', models.DateTimeField(auto_now=True)),
                ('created_news', models.DateTimeField(auto_now_add=True)),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.Status', verbose_name='Статус новости')),
            ],
            options={
                'ordering': ['-created_news'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя комментатора')),
                ('text_comment', models.TextField(verbose_name='Текст комментария')),
                ('created_comment', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('id_news', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.News')),
            ],
            options={
                'ordering': ['-created_comment'],
            },
        ),
    ]