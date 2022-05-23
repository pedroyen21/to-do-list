from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date',  'conc_date', )
   
admin.site.register(Task, TaskAdmin)