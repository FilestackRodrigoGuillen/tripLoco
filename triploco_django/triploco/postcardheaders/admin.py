from django.contrib import admin
from postcardheaders.models import PostCardHeader
# Register your models here.

@admin.register(PostCardHeader)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user','photo_cover','cover_workflow','photo_flag','location_link','photo_weather','ocr_workflow','photo_polaroid']
