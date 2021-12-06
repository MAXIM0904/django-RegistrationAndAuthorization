from django.forms import ModelForm, CharField, PasswordInput
from .models import News, Comment


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text_comment', )


class AuthForm(ModelForm):
    user_name = CharField()
    password = CharField(widget=PasswordInput)
