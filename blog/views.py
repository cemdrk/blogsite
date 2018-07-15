from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.order_by('created')
    return render(request, 'blog/home.html', {'posts': posts})

def post_details(request, slug):
    post = get_object_or_404(Post, slug= slug)
    return render(request, 'blog/post_details.html', {'post': post})
