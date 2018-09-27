from django.shortcuts import render, redirect
from data.models import Project
import data.forms as forms
from django.urls import reverse

# Create your views here.

def Portfolio(request):
    projects = Project.objects.all()
    return render(request, 'data/projects.html', {'projects':projects})

def addProject(request):
    projectForm = forms.ProjectForm()

    if request.method == 'POST':
       
        projectForm = forms.ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            newProject = Project()
            newProject.title = request.POST.get('title')
            newProject.description = request.POST.get('description')
            newProject.image = projectForm.cleaned_data['image']
            newProject.link = request.POST.get('link')
            newProject.save()
            return redirect(reverse('projects'))
        
    return render(request, 'data/addProject.html', {'project':projectForm})