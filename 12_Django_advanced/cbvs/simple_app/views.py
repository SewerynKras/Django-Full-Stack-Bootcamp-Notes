from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from simple_app import models
from django.urls import reverse_lazy


class IndexCBV(TemplateView):
    template_name = 'simple_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = "Seweryn"
        return context


class SchoolListView(ListView):
    model = models.School
    template_name = "simple_app/list.html"
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = models.School
    template_name = "simple_app/detail.html"
    context_object_name = 'school_detail'


class StudnetCreateView(CreateView):
    model = models.Student
    fields = ['name', 'age', 'school']
    template_name = 'simple_app/create.html'


class StudentUpdateView(UpdateView):
    model = models.Student
    template_name = 'simple_app/create.html'
    fields = ['age', 'school']


class StudentDeleteView(DeleteView):
    model = models.Student
    template_name = 'simple_app/delete.html'
    success_url = reverse_lazy('simple_app:list')
