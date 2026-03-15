from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about_me, name="about_me"),
    path("projects/",views.project,name="project"),
    path("skills/",views.skill,name="skill"),
    path("contact/",views.contact,name="contact"),
]
