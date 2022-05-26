from django.shortcuts import render
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class IndexView(generic.ListView, LoginRequiredMixin):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['tasks'] = context['tasks'].filter(user=self.request.user).order_by('conc_date')
            context['count'] = context['tasks'].filter(concluded=True).count()
        else:
            context = {}
        return context


