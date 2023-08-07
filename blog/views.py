from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from django.core.paginator import Paginator


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status = 1, category__name = kwargs['cat_name'])
    # paginator = Paginator(posts, 3)
    # page_number = request.GET.get("page")
    content = {'posts' : posts}
    return render(request, 'blog/blog.html', content)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, status=1, id=pid)
    category = Category.objects.all()
    categories = {}
    for cat in category:
        if cat.name not in categories:
            categories[cat.name] = 1
        
        else:
            categories[cat.name] += 1

    content = {'post':post, 'categories':categories}
    return render(request, 'blog/single.html', content)

def search_view(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    content = {'posts' : posts}
    return render(request, 'blog/single.html', content)
