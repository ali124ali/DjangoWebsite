from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'home'),
    # path('single/', blog_single_view, name = 'single'),
]