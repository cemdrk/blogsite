from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.order_by('created')
    return render(request, 'blog/index.html', {'posts': posts})
