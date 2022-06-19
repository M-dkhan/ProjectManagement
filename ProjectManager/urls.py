from django.urls import path
from . import views 

urlpatterns = [
    path('add-project', views.add_project, name='add-project'),
    path('project/<slug:slug>', views.project_detail, name='project-detail'),
]
