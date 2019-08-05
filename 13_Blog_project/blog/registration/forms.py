from django import forms
from registration.models import Author, User


class BasicRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)
    email_verify = forms.EmailField(required=True, label='Email (again):')

    def clean(self):
        form = super().clean()

        if form['email'] != form['email_verify']:
            raise forms.ValidationError("Emails don't match")
        if User.objects.filter(email=form['email']).exists():
            raise forms.ValidationError("A user with that email already exists")

    class Meta():
        model = User
        fields = ['username', 'password', 'email']

    field_order = ['username', 'password', 'email', 'email_verify']


class AuthorRegistrationForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)

    class Meta():
        model = Author
        fields = ['profile_pic']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
