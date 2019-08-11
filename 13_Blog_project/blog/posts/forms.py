from django import forms
from posts import models


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, required=True, label="",
                           widget=forms.Textarea)

    class Meta:
        model = models.Comment
        fields = ['text']
