from django.shortcuts import render
from .models import Post, Comment


def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('-published_date')
    # comments = Comment.objects.filter(approved=True, post=pk)
    content = {'posts' : posts}
    return render(request, 'blog/blog.html', content)

def blog_single_view(request):
    return render(request, 'blog/single.html')