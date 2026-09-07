from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,About, Skill, Contact
from rag.rag import ask_rag
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse
def home(request):
    about=About.objects.first()
    try:
            skill=Skill.objects.all()
    except:
            print("invalid")
    try:
            project=Project.objects.all()
    except:
            print("invalid")
    return render(request, 'home.html',{'about':about,'project' : project,'skill':skill})

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

def ai_assistant(request):
     return render(request, "ai_assistant.html")


@csrf_exempt
def chat_api(request):

    if request.method == "POST":

        try:
            question = request.POST.get("question")

            print("QUESTION:", question)

            answer = ask_rag(question)

            print("ANSWER:", answer)

            return JsonResponse({
                "answer": answer
            })

        except Exception as e:

            print("ERROR:", e)

            return JsonResponse({
                "error": str(e)
            }, status=500)

    return JsonResponse({
        "error": "Only POST requests are allowed."
    }, status=405)