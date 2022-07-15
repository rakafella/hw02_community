from django.shortcuts import render, get_object_or_404
from .models import Post, Group, Number_of_posts


def index(request):
    posts = Post.objects.all()[:Number_of_posts]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:Number_of_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
