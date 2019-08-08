from django import forms
from registration.models import Author, User
from string import ascii_lowercase, ascii_uppercase, digits


def validate_username(username):
    """
    Every username should:
    1. Be unique (case insensitive)
    2. Have between 5 and 16 characters
    3. Contain only letters and numbers
    """
    valid_characters = ascii_lowercase+ascii_uppercase+digits
    for char in username:
        if char not in valid_characters:
            raise forms.ValidationError("Only letters and numbers are allowed")

    if not (5 <= len(username) <= 16):
        raise forms.ValidationError("Usernames should be between 5 and 16 characters")

    duplicate_username = User.objects.filter(username__iexact=username)
    if duplicate_username.exists():
        raise forms.ValidationError("A user with that username is already registered")

    return username


class BasicRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=16, required=True, validators=[validate_username])
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
    username = forms.CharField(max_length=16, required=False, validators=[validate_username])
    profile_pic = forms.ImageField(required=False)
