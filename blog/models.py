from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog', default = 'blog/default.jpg')
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(null= False, blank=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name