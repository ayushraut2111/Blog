from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogRegister(admin.ModelAdmin):
    list_display=['id','Author','created_at','updated_at']
