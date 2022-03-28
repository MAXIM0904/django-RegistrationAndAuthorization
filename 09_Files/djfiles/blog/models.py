from django.db import models


class BlogEntry(models.Model):
    '''
    Класс модель блога. Содержит поля автор, заголовок блога, тест записи и дату создания записи.
    '''
    author = models.CharField(max_length=100, verbose_name="Автор записи")
    record_title = models.CharField(max_length=200, verbose_name="Заголовок записи")
    record_text = models.TextField(verbose_name="Текст записи")
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.record_title


class UploadingFiles(models.Model):
    '''
    Класс для множественного сохранения файлов. Содержит поля:
    file - для сохранения файлов. Принимает файлы Image.
    model_file - для связи один ко многим с моделью BlogEntry.
    '''
    file = models.ImageField(upload_to='blog_img', verbose_name='Загрузка изображения', blank=True)
    model_file = models.ForeignKey('BlogEntry', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.file)
