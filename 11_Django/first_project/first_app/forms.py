from django import forms
from django.core import validators


def custom_validator(value):
    if value[0].lower() != "s":
        raise forms.ValidationError("Name should start with 's'")
    return value


class BasicForm(forms.Form):
    name = forms.CharField(validators=[custom_validator])
    email = forms.EmailField()
    email_valid = forms.EmailField(label="Email again:")
    text = forms.CharField(widget=forms.Textarea)
    # empty form field used to counter brainless bots
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # validate all values at once
    def clean(self):
        form = super().clean()

        if form['email'] != form['email_valid']:
            raise forms.ValidationError("Emails dont match >:-(")
