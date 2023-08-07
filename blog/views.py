from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True).order_by('-published_date')
    if kwargs['cat_name'] != None:
        posts = Post.objects.filter(status = 1, category__name = kwargs['cat_name'])
    # paginator = Paginator(posts, 3)
    # page_number = request.GET.get("page")
    content = {'posts' : posts}
    return render(request, 'blog/blog.html', content)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, id=pid)
    content = {'post':post}
    return render(request, 'blog/single.html', content)
