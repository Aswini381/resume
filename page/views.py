from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,About, Skill, Contact
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about_me(request):
    about=About.objects.first()
    return render(request,'about.html',{'about':about})

    
def project(request):
    try:
        project=Project.objects.all()
    except:
        print("invalid")
    
    return render(request,'project.html',{'project': project})

def skill(request):
    try:
        skill=Skill.objects.all()
    except:
        print("invalid")

    return render(request,'skill.html',{'skill':skill})

def contact(request):
    contact=Contact.objects.all()
    return render(request,'contact.html',{'contact':contact})