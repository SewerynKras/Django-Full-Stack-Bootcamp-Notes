from django.views.generic import TemplateView, View, DetailView
from registration import forms
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from registration import models


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['basic_user_form'] = forms.BasicRegisterForm
        context['extended_user_form'] = forms.AuthorRegistrationForm
        context['errors'] = []
        context['registered'] = False
        return context

    def post(self, request):
        basic_user = forms.BasicRegisterForm(request.POST)
        extended_user = forms.AuthorRegistrationForm(request.POST)

        registered = False
        errors = []

        if basic_user.is_valid() and extended_user.is_valid():
            user = basic_user.save()
            user.set_password(user.password)
            user.save()

            ext_user = extended_user.save(commit=False)
            ext_user.user = user

            if 'profile_pic' in request.FILES:
                image = request.FILES['profile_pic']
                #image = image.resize(settings.IMAGE_SIZE)  #FIXME: image is a "InMemoryUploadedFile"
                ext_user.profile_pic = image

            ext_user.save()

            registered = True
        else:
            for message in basic_user.errors.values():
                errors.append(message)
            for message in extended_user.errors.values():
                errors.append(message)

        context = self.get_context_data()
        context['registered'] = registered
        context['errors'] = errors

        return render(request, self.template_name, context=context)


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['login_form'] = forms.LoginForm()
        return context

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # go back to the homepage
            return redirect("/")
        else:
            context = self.get_context_data()
            context['incorrect_data'] = True
            return render(request, self.template_name, context=context)


class LogoutView(LoginRequiredMixin, View):

    login_url = "/user/login"

    def get(self, request):
        logout(request)
        return redirect("/")


class ProfileView(DetailView):
    template_name = "registration/profile.html"
    model = models.Author
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_author = self.get_object()
        logged_user = self.request.user

        if selected_author.user == logged_user:
            context["edit_form"] = forms.EditProfileForm()
        return context

    def post(self, request, slug):
        # double check that this is the correct author
        selected_author = self.get_object()
        logged_user = self.request.user

        if selected_author.user == logged_user:
            edit_form = forms.EditProfileForm(request.POST)

            if edit_form.is_valid():
                if edit_form.username:
                    logged_user.username = edit_form.username
                if edit_form.profile_pic:
                    selected_author.profile_pic = edit_form.profile_pic
                selected_author.save()
                #TODO: redirect to new page
            else:
                #TODO: return invalid_data like in login
        
        else:
            #TODO: return FORBIDDEN
