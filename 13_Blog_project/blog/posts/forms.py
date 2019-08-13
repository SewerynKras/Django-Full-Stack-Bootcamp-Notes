from django import forms
from posts import models


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, required=True, label="",
                           widget=forms.Textarea)

    class Meta:
        model = models.Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, required=True, label="",
                            widget=forms.HiddenInput(attrs={'id': 'actual_title'}))
    text = forms.CharField(required=True, label="",
                           widget=forms.HiddenInput(attrs={'id': 'actual_text'}))

    class Meta:
        model = models.Post
        fields = ['title', 'text']
