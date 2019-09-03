from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
from . import models


# just index 
class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['hereval'] = "HERE IS SERVER SIDE VALUE"
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School
    template_name = 'app/school_form.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("app:list")

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based View are Cool!')