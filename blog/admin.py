from django.contrib import admin
from .models import Post, Comment, Ticket, Event
from django_summernote.admin import SummernoteModelAdmin


#Show Published / Draft clearly in admin list
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", 'slug', "author", "created_on")
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
# Register your models here.
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(Event)

