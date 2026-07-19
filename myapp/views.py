from django.shortcuts import render
from .models import Skill,Project
def home (request):
    skills = Skill.objects.all()
    context = {
        'username': 'አብዱሮህማን ' ,
        'role': 'የወደፊቱ ባለሙያ Full-stack Developer ',
        'skills':skills
        }
    return render(request, 'home.html',context)
def about(request):
    return render (request, 'about.html')
def greet_user(request,name):
    context = {'user_name': name}
    return render(request,'greet.html',context)
def projects_list(request):
    projects = Project.objects.all()
    context = { 'projects':projects}
    return render(request,'projects.html',context)