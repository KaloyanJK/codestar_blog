from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    # 'pagination tells' Django to display the posts 6 at a time
    paginate_by = 6