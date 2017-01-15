from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/index.html', {'questions': questions})

def results(request):
    questions = Question.objects.all() 
    score = 0
    for question in questions:
        answer = question.correct_answer 
        entered_answer = request.POST.get(str(question.number)) #fetches entered answer by the candidate
        if(entered_answer == answer): 
            score+=1 
    score*=5
    return render(request, 'app/results.html', {'score':score})
    
