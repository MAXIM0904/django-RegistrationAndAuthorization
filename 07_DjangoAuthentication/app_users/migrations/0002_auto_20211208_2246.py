# Generated by Django 2.2 on 2021-12-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Имя пользователя'),
        ),
    ]
