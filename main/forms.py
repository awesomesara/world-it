from datetime import datetime

from django import forms

from main.models import *


class PostForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Post
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        self.post_id = kwargs.pop('post_id', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['body', ]

    def save(self, commit=True):
        user = super(CommentForm, self).save(commit=False)
        post = super(CommentForm, self).save(commit=False)
        user.user_id = self.user_id
        post.post_id = self.post_id
        if commit:
            user.save()
        return user