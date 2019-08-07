from django import forms
from registration.models import Author, User


def check_duplicate_username(username):
    """every username should be unique (case insensitive)"""
    duplicate_username = User.objects.filter(username__iexact=username)
    if duplicate_username.exists():
        raise forms.ValidationError("A user with that username is already registered")
    return username


class BasicRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=32, required=True, validators=[check_duplicate_username])
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


class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=32, required=False, validators=[check_duplicate_username])
    profile_pic = forms.ImageField(required=False)
