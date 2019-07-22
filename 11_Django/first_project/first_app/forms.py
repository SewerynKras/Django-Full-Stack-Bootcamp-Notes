from django import forms
from django.core import validators
from first_app.models import User


def custom_validator(value):
    if any(i.isdigit() for i in value):
        raise forms.ValidationError("Name should not contain digits!")
    return value


class NewUserForm(forms.ModelForm):
    name = forms.CharField(validators=[custom_validator])
    email = forms.EmailField()
    email_valid = forms.EmailField(label="Email again:")
    # empty form field used to counter brainless bots
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # validate all values at once
    def clean(self):
        form = super().clean()

        if form['email'] != form['email_valid']:
            raise forms.ValidationError("Emails dont match >:-(")

    class Meta:
        model = User
        fields = '__all__'
