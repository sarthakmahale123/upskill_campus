from django.contrib import admin
from .models import ShortURL
# Register your models here.


class URLAdmin(admin.ModelAdmin):
    list_display = ['id','original_url','short_url','date_time_created']

admin.site.register(ShortURL,URLAdmin)