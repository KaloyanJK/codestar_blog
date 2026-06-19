from django.contrib import admin
from .models import Post, Comment, Ticket, Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "status", "slug", "author", "created_on")
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(Event)