from django.contrib import admin
from .models import Video, Comment, Channel, Like, Dislike, Video_View, Channel_Subscription, Stream
# Register your models here.

admin.site.register([Stream, Comment, Channel, Like, Dislike, Video_View, Channel_Subscription])


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "path", "datetime", "user", "number_of_views")
	fields = list_display
