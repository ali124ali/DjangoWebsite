from django.shortcuts import render
from blog.models import Post, Category
from datetime import datetime
from website.forms import ContactForm
from django.contrib import messages

def home_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now())[:3]
    fav_posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by("-view_count")[:3]
    future = Post.objects.filter(status=1, published_date__gt=datetime.now())[:1]

    if not future:
        future = None

    category = Category.objects.all()


    content = {'posts' : posts, 'category' : category, 'fave_posts' : fav_posts, 'future':future}
    return render(request, 'website/index.html', content)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Ticket Submited Successfully')

        else:
            messages.add_message(request, messages.ERROR, 'Something Wrong')
    form = ContactForm(request.POST)

    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')
