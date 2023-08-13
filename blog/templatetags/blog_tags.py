from django import template
from blog.models import Post, Category
from datetime import datetime

register = template.Library()

# return total number of published posts
@register.simple_tag(name='totalposts')
def function():
    total = Post.objects.filter(status=1, published_date__lte=datetime.now()).count()
    return total

# counting categories that used for posts
@register.simple_tag(name='catcounter')
def function():
    total = Post.objects.filter(status=1)
    category = Category.objects.all()
    categories = {}
    
    for cat in category:
        categories[cat.name] = 0

    for post in total:
        for cat in post.category.all():
            categories[cat.name] += 1

    return categories.items()
