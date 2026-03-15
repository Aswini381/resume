from django.contrib import admin
from .models import Category, Project, About, Skill, Contact
# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Contact)