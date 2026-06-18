from django.contrib import admin
from .models import Post, Comment, Ticket, Event


# Register your models here.
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(Event)

#Show Published / Draft clearly in admin list
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "author", "created_on")