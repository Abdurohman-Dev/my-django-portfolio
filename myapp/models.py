from django.db import models
class Skill(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"መልዕክት ከ {self.name}"
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    recommended_by = models.CharField(max_length=50)
    def __str__(self):
        return self.title