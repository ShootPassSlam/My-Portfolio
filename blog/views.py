from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.core.cache import cache

from .models import Post

POSTS_KEY = "posts.all"

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'    

    def get_queryset(self):
        posts = cache.get(POSTS_KEY)
        if not posts:
            print("NOTHNG CACHED")
            posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
            cache.set(POSTS_KEY, posts)
        for post in posts:
            print(post.post_title)
        return posts

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())