from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    lasst_name = models.CharField(max_length=30)
    email = models.EmailField()

class Article(models.Model):
    first_name = models.CharField(max_length=30)
    lasst_name = models.CharField(max_length=30)
