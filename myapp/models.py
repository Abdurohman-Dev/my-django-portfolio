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