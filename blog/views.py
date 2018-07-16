from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.order_by('created')
    return render(request, 'blog/home.html', {'posts': posts})

def post_details(request, slug):
    post = get_object_or_404(Post, slug= slug)
    return render(request, 'blog/post_details.html', {'post': post})

def post_create(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')
        return render(request, 'blog/post_create.html', context)
    else:
        return HttpResponseRedirect('/login')

def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/')
