from django.views.generic import TemplateView, ListView, DetailView
from simple_app import models


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
