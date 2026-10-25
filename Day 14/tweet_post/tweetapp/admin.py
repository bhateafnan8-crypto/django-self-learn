from django.contrib import admin
from .models import TweetModel
# Register your models here.

@admin.register(TweetModel)
class TweetModelAdmin(admin.ModelAdmin):
    list_display = ['text','photo']
    search_fields = ['user','text']