from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'home'),
    path('post/<int:pid>', blog_single_view, name = 'single'),
    path('category/<str:cat_name>', blog_view, name = 'category'),
    path('tag/<str:tag_name>', blog_view, name = 'tag'),
    path('search/', search_view, name = 'search')
]