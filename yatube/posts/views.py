from itertools import count
from unicodedata import name
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, Number_of_posts, User
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, Number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    paginator = Paginator(posts, Number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    username = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=username)
    paginator = Paginator(posts, Number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count_page = posts.count()
    context = {
        'username': username,
        'page_obj': page_obj,
        'count_page': count_page
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'posts/post_detail.html', context)