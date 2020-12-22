""" Posts admin classes """

#Django
from django.contrib import admin

# Models
from posts.models import Posts

# Register your models here
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'website', 'details', 'photo',)
    list_editable = ('website','photo')