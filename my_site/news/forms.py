from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeField


class ActiclesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            # 'category': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Категория'
            # }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }