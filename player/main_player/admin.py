from django.contrib import admin
from .models import *

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'file', 'create_at', 'slug']
    prepopulated_fields = {'slug': ('title',)}