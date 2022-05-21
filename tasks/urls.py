from django.urls import path
from . import views
 
app_name = 'tasks'
urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index',
    )
]