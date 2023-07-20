from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
   list_display = ('author', 'title','view_count','status','login_required','created_date', 'published_date', 'updated_date')
   list_filter = ('status', 'login_required')
   search_fields = ('title', 'content', 'category')

   ordering = ('published_date',)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email')
    list_filter = ('approved',)

    search_fields = ('subject', 'message')



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
