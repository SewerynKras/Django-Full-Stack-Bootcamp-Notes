from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts import models
from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from datetime import datetime
from posts import forms


class IndexView(ListView):
    template_name = "posts/index.html"
    model = models.Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.model.objects.filter(draft=False).order_by('-date_published')
        return query


class NewPostView(CreateView):
    template_name = "posts/create_post.html"
    model = models.Post
    fields = ['title', 'text']

    def form_valid(self, form):
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        author = self.request.user.author
        draft = True

        post = models.Post(title=title, text=text,
                           author=author, draft=draft)

        post.save()
        return redirect("/")


class DraftView(ListView):
    template_name = 'posts/drafts.html'
    model = models.Post
    context_object_name = "posts"

    def get_queryset(self):
        author = self.request.user.author
        query = self.model.objects.filter(author=author, draft=True)
        return query


class UpdateDraft(UpdateView):
    model = models.Post
    template_name = 'posts/edit_post.html'
    fields = ['title', 'text']

    def dispatch(self, request, *args, **kwargs):
        if request.user.author != self.get_object().author:
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)


class PublishDraft(DetailView):
    model = models.Post
    template_name = "posts/preview_post.html"
    context_object_name = "post"

    def dispatch(self, request, *args, **kwargs):
        if request.user.author != self.get_object().author:
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['publish'] = True
        return context

    def post(self, request, slug):
        post = self.get_object()
        post.draft = False
        post.date_published = datetime.now()
        post.save()
        return redirect("/")


class DeleteDraft(DeleteView):
    model = models.Post
    template_name = "posts/preview_post.html"
    context_object_name = "post"
    success_url = "/drafts"

    def dispatch(self, request, *args, **kwargs):
        if request.user.author != self.get_object().author:
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['delete'] = True
        return context


class PostView(DetailView):
    model = models.Post
    template_name = "posts/preview_post.html"
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_comment_form'] = forms.CommentForm()
        comments = models.Comment.objects.filter(post=self.get_object())
        context['comments'] = comments
        context['num_comments'] = len(comments)
        return context

    def post(self, request, slug):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            text = comment_form.cleaned_data['text']
            author = self.request.user.author
            post = self.get_object()
            comment = models.Comment(text=text, author=author, post=post)
            comment.save()
            return redirect("posts:post", slug=slug)
        else:  # if form is invalid
            errors = []
            for message in comment_form.errors.values():
                errors.append(message)
            context = self.get_context_data()
            context['comment_form_errors'] = errors
            return render(request, self.template_name, context=context, slug=slug)
