from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
   path(
      route='',
      view=views.IndexView.as_view(),
      name='index',
   ),
   path(
      route='create_task',
      view=views.create_task,
      name='create_task',
   ),
   path(
      route='task_confirm_delete/<int:pk>',
      view=views.DeleteTask.as_view(),
      name='task_confirm_delete',
   ),
   path(
      route='edit_task/<int:pk>',
      view=views.EditTask.as_view(),
      name='edit_task',
   ),
   path(
      route='conclude_task/<int:pk>',
      view=views.conclude_task,
      name='conclude_task',
   )

]