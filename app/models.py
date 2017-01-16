from django.db import models
from django.utils import timezone



class Question(models.Model):
   
    number=models.CharField(max_length=200)
    Question = models.TextField()
    Choice1 = models.CharField(max_length=200)
    Choice2 = models.CharField(max_length=200)
    Choice3 = models.CharField(max_length=200)
    Choice4 = models.CharField(max_length=200)
    Choice5 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def publish(self):
      
        self.save()

    def __str__(self):
        return self.number

