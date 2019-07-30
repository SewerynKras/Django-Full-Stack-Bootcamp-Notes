from django import forms
from registration.models import Author, User


class BasicRegisterForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)
    email_verify = forms.EmailField(required=True)

    def clean(self):
        form = super().clean()

        if form['email'] != form['email_verify']:
            raise forms.ValidationError("Emails don't match")

    class Meta():
        model = User
        fields = ['username', 'password', 'email']

    field_order = ['username', 'password', 'email', 'email_verify']


class AuthorRegistrationForm(forms.Form):
    class Meta():
        model = Author
        fields = ['profile_pic']
