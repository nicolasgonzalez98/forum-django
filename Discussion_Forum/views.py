from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    forums = Forum.objects.all()
    count = forums.count()

    
    
    ctx = {
        'forums': forums,
        'count':count
    }
    return render(request, 'home.html', ctx)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    ctx = {
        'form':form
    }
    return render(request, 'addInForum.html', ctx)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    ctx = {
        'form':form
    }
    return render(request, 'addInDiscussion.html', ctx)