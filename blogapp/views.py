from django.shortcuts import render

from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html', {'posts': posts})

def singlePost(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'post.html', {'instance': post})