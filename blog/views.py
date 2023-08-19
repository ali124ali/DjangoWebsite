from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from datetime import datetime
from blog.forms import CommentForm
from django.contrib import messages


# view for blog home page
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now())

    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status = 1, category__name = kwargs['cat_name'])

    if kwargs.get('tag_name') != None:
        posts = Post.objects.filter(status = 1, tags__name = kwargs['tag_name'])
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
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Comment Has Sent Succussfully and Will Published ASAP')
        else:
            messages.add_message(request, messages.ERROR, 'Somthing Wrong, Please Check Your Info Again.')

    form = CommentForm()

    posts = Post.objects.filter(status=1, published_date__lte=datetime.now())
    posts = list(posts)
    post = get_object_or_404(Post, status=1, id=pid)
    comments = Comment.objects.filter(approved=1, post=pid)
    comments_count = comments.count()

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

    content = {'post':post, 'next':next, 'prev': prev, 'comments':comments, 'comments_count':comments_count ,'form':form}
    return render(request, 'blog/single.html', content)

# search field in blog page
def search_view(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
        else:
            posts = None

    content = {'posts' : posts}
    return render(request, 'blog/single.html', content)
