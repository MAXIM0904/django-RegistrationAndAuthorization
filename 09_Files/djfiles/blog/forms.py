from django.forms import ModelForm, FileField, ClearableFileInput, Form
from .models import BlogEntry, UploadingFiles



class BlogRecordForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = ('record_title', 'record_text', )

class UploadingFilesForm(ModelForm):
    class Meta:
        model = UploadingFiles
        fields = ('file', )
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True})
        }

class MassiveBlogUpdateForm(Form):
    blog_file = FileField()
