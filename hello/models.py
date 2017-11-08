from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
