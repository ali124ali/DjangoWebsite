from django.shortcuts import render
from blog.models import Post, Category
from datetime import datetime

def home_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by("-published_date")[:3]
    category = Category.objects.all()

    content = {'posts' : posts, 'category' : category}
    return render(request, 'website/index.html', content)

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')
