from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from .forms import UpdateForm

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

def delete_task(request, pk):
   task_to_be_deleted = Task.objects.get(id=pk)
   task_to_be_deleted.delete()
   return HttpResponseRedirect('/')

class EditTask(UpdateView):
   template_name = 'tasks/edit_task.html'
   form_class    = UpdateForm
   success_url   = '/'
   model = Task

    
