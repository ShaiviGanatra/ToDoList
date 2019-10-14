from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    incharge = models.CharField(max_length=100)
    submission_date = models.DateField()

