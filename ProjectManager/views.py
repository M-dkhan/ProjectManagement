from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from ProjectManager.models import Project

# Create your views here.
def home(request):
    return render(request, 'ProjectManager/home.html')

def all_project(request):
    pass

def add_project(request, slug):
    project = Project.objects.filter(slug__iexact = slug)
    if project.exists():
        # logic here
        pass 
    else:
        return HttpResponse('<h1>404 Project Not Found </h1>')
    pass
        
def project_detail(request):
    pass
