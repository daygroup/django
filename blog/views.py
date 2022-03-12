from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def create_post(request):
    me = User.objects.get(username='admin')
    for i in range(100):
        Post.objects.create(author=me, title=f'Sample title{i}', text=f'Test{i}')

    