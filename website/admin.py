from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('created_date',)

    search_fields = ('subject', 'content')


admin.site.register(Contact, ContactAdmin)