from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        head = cleaned_data.get('head')
        body = cleaned_data.get('body')
        if head == body:
            raise ValidationError(
                'Основной текст не должен быть идентичен заголовку'
            )

        return cleaned_data
