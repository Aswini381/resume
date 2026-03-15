from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class About(models.Model):
    
    about_heading=models.CharField(max_length=25,blank=True, null=True)
    about_description = models.TextField(default="This is the about section description.")

    def __str__(self):
        return self.about_heading
    
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=5000)
    link=models.URLField(unique=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    skill=models.CharField(max_length=50)

    def __str__(self):
        return self.skill
    
class Contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_link=models.URLField(unique=True)

    def __str__(self):
        return self.contact_name