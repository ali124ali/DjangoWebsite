from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(SummernoteModelAdmin):
  list_display = ('author', 'title','view_count','status','login_required','created_date', 'published_date', 'updated_date')
  list_filter = ('status', 'login_required')
  search_fields = ('title', 'content', 'category')
  summernote_fields = ('content', 'title')

  ordering = ('published_date',)



class CommentAdmin(admin.ModelAdmin):
  list_display = ('post', 'name', 'email')
  list_filter = ('approved',)

  search_fields = ('subject', 'message')



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
