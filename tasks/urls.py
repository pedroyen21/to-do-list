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
      route='delete_task/<int:pk>',
      view=views.delete_task,
      name='delete_task',
   ),
   path(
      route='edit_task/<int:pk>',
      view=views.EditTask.as_view(),
      name='edit_task',
   ),

]