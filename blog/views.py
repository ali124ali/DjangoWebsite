from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from datetime import datetime


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True, published_date__lte=datetime.now()).order_by('-published_date')

    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status = 1, category__name = kwargs['cat_name'])

    # create pagination of blog
    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)

    except EmptyPage:
        posts = posts.get_page(1)

    except PageNotAnInteger:
        posts = posts.get_page(1)

    except InvalidPage:
        posts = posts.get_page(1)

    content = {'posts' : posts}
    return render(request, 'blog/blog.html', content)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, status=1, id=pid)
    # posts_cat = Post.
    category = Category.objects.all()
    categories = {}
    for cat in category:
        if cat.name not in categories:
            categories[cat.name] = 1
        
        else:
            categories[cat.name] += 2

    content = {'post':post, 'categories':categories}
    return render(request, 'blog/single.html', content)

def search_view(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    content = {'posts' : posts}
    return render(request, 'blog/single.html', content)
