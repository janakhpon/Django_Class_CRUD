from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['hereval'] = "HERE IS SERVER SIDE VALUE"
        return context

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'app/detail.html'

class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = model.School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

class SchooDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("app:list")

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based View are Cool!')