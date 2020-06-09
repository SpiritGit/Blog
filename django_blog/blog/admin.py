from django.contrib import admin
from .models import Post, Text

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['title','date_posted','author']
    list_filter = ['author','date_posted']
    search_fields = ['date_posted']
    list_per_page = 10

admin.site.register(Text)
admin.site.register(Post,Admin)