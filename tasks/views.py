from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UpdateForm

class IndexView(generic.ListView, LoginRequiredMixin):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['todo_tasks'] = context['tasks'].filter(concluded=False).order_by('conc_date')
            context['concluded_tasks'] = context['tasks'].filter(concluded=True).order_by('pub_date')
            context['count'] = context['tasks'].filter(concluded=True).count()
        else:
            context = {}
        return context

@login_required
def create_task(request):
   if request.method == 'POST':
      new_task = Task.objects.create(
               user        =request.user, 
               name        =request.POST['name'], 
               description =request.POST['description'],
               conc_date   =request.POST['conc_date']
      )
      new_task.save()
   return HttpResponseRedirect('/')

class EditTask(UpdateView):
   template_name = 'tasks/edit_task.html'
   model = Task
   form_class = UpdateForm
   success_url = '/'

class DeleteTask(DeleteView):
   template_name = 'tasks/task_confirm_delete.html'
   model = Task
   success_url = reverse_lazy('tasks:index')
   
def conclude_task(request, pk):
   if request.method == 'POST':
      task = Task.objects.get(id=pk)
      task.concluded = True
      task.save()
   return HttpResponseRedirect('/')




    
