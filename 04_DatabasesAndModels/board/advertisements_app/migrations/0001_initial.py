# Generated by Django 2.2 on 2021-11-15 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.IntegerField(default=0, verbose_name='номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500)),
                ('description', models.TextField(default='', verbose_name='описание')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('price', models.FloatField(default=0, verbose_name='цена')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('status_author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.Author')),
                ('status_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.Category')),
            ],
        ),
    ]
