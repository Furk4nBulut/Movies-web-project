from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','isPublished')
    list_display_links = ('id','name')
    list_filter = ('created_date','id')
    list_editable = ('isPublished',)
    search_fields = ('name','description')
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)