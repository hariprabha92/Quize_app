from django.db import models
from django.utils import timezone



class Question(models.Model):
   # author = models.ForeignKey('auth.User')
    number=models.CharField(max_length=200)
    Question = models.TextField()
    Choice1 = models.CharField(max_length=200)
    Choice2 = models.CharField(max_length=200)
    Choice3 = models.CharField(max_length=200)
    Choice4 = models.CharField(max_length=200)
    Choice5 = models.CharField(max_length=200)
    # = models.CharField(max_length=200)



   # created_date = models.DateTimeField(
   #         default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.number

