from django import forms
from django.core import validators
from first_app.models import ExtendedUser
from django.contrib.auth.models import User


def custom_validator(value):
    if any(i.isdigit() for i in value):
        raise forms.ValidationError("Name should not contain digits!")
    return value


class NewUserForm(forms.ModelForm):
    username = forms.CharField(validators=[custom_validator])
    email = forms.EmailField()
    email_valid = forms.EmailField(label="Email again:")
    # empty form field used to counter brainless bots
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    password = forms.CharField(widget=forms.PasswordInput)

    # validate all values at once
    def clean(self):
        form = super().clean()

        if form['email'] != form['email_valid']:
            raise forms.ValidationError("Emails dont match >:-(")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    field_order = ['username', 'password', 'email', 'email_valid']


class ExtendedUserForm(forms.ModelForm):
    class Meta():
        model = ExtendedUser
        fields = ["profile_pic"]
