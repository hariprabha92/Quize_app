#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
#from .forms import PostForm
#from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
#from .models import Post
from .models import Question

def home(request):
    posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/index.html', {'posts': posts})

