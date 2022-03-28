from _csv import reader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import BlogEntry, UploadingFiles
from .forms import BlogRecordForm, UploadingFilesForm, MassiveBlogUpdateForm

class RecordBlogListView(ListView):
    '''Класс выводит все записи блога на экран пользователя'''
    model = BlogEntry
    template_name = 'blog/record_list.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    ''' Класс создания новости '''
    model = BlogEntry
    file_model = UploadingFiles
    form_class = BlogRecordForm
    from_file_class = UploadingFilesForm


    def get(self, request, *args, **kwargs):
        ''' Функция вызывает формы BlogRecordForm и UploadingFilesForm и передает их в шаблон '''
        self.object = self.form_class()
        form_img = self.from_file_class()
        return render(request, 'blog/createview.html', {'form': self.object, 'form_img': form_img})

    def post(self, request, *args, **kwargs):
        '''
        Функция получает из шаблона введенные пользователем данные
        и сохраняет их в bd моделей BlogEntry и UploadingFiles
        '''
        form = self.form_class(request.POST)
        form_files = self.from_file_class(request.POST, request.FILES)
        if form.is_valid() and form_files.is_valid():
            author = request.user
            record_title = form.cleaned_data['record_title']
            record_text = form.cleaned_data['record_text']
            form_instance = BlogEntry.objects.create(
                author = author,
                record_title = record_title,
                record_text = record_text,
            )
            files = form_files.files.getlist('file')
            for i_f in files:
                file_instanse = UploadingFiles(file=i_f, model_file=form_instance)
                file_instanse.save()
            return redirect('/')


class BlogDetailView(DetailView):
    ''' Класс выводит выбранную пользователем запись блога для просмотра '''
    model = BlogEntry
    model_file = UploadingFiles
    template_name = 'blog/record_detail.html'

    def get(self, request, *args, **kwargs):
        ''' Функция получает get-запрос и возвращает формы UploadingFiles и BlogEntry для просмотра '''
        self.object = BlogEntry.objects.get(id=kwargs['pk'])
        file_user = UploadingFiles.objects.filter(model_file_id=kwargs['pk'])
        return self.render_to_response(self.get_context_data(object=self.object, file_user=file_user))


def massive_blog_update(request):
    ''' Функция позволяет массово добавлять записи в блог. Использует формат .cvs '''
    if request.user.is_authenticated:
        if request.method == "POST":
            update_blog_form = MassiveBlogUpdateForm(request.POST, request.FILES)
            if update_blog_form.is_valid():
                blog_file = update_blog_form.cleaned_data['blog_file'].read()
                blog_file_str = blog_file.decode('utf-8').split('\n')
                csv_reader = reader(blog_file_str, delimiter=',', quotechar='"')
                for row in csv_reader:
                    if row:
                        row = row[0].split(';')
                        BlogEntry.objects.create(
                            author=request.user,
                            record_title="Дополнить заголовок",
                            record_text=row[0],
                            creation_date = row[1]
                        )
                return HttpResponse(content="Записи успешно добавлены", status=200)
        else:
            form = MassiveBlogUpdateForm()
            return render(request, 'blog/massive_blog_update.html', {'form': form})
    else:
        return redirect("profile/login_user")