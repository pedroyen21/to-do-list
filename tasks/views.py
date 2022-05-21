from django.shortcuts import render
from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView, LoginRequiredMixin):
    model = Task
    template_name = 'tasks/index.html'

