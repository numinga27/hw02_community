from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User
from .constats import MAX_POSTS


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, MAX_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:MAX_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts_list = Post.objects.filter(author=user)
    posts_count = Post.objects.filter(author=user).count()
    paginator = Paginator(posts_list, MAX_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'user': User,
               'posts_list': posts_list,
               'page_obj': page_obj,
               'posts_count': posts_count,
               }

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts_count = Post.objects.filter(author=post.author).count
    context = {'post': post,
               'posts_count': posts_count
               }

    return render(request, 'templates/posts/post_detail.html', context)
