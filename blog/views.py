from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from datetime import datetime

# view for blog home page
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')

    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status = 1, category__name = kwargs['cat_name'])

    # create pagination of blog posts
    posts = Paginator(posts, 6)

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

# view for blog single page
def blog_single_view(request, pid):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')
    posts = list(posts)
    post = get_object_or_404(Post, status=1, id=pid)

    index = posts.index(post)
    if index == 0:
        prev = None
        next = posts[index + 1]
    
    elif index == len(posts) - 1:
        next = None
        prev = posts[index - 1]

    else:
        next = posts[index + 1]
        prev = posts[index - 1]

    if post:
        post.view_count += 1
        post.save()

    content = {'post':post, 'next':next, 'prev': prev}
    return render(request, 'blog/single.html', content)

# search field in blog page
def search_view(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    content = {'posts' : posts}
    return render(request, 'blog/single.html', content)
