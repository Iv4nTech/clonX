from django.shortcuts import render
from .models import Post, User

def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed/feed.html', {'posts':posts})