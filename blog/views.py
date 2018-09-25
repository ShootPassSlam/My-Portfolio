from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.core.cache import cache

import time

from .models import Post

POSTS_KEY = "posts.all"

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'    
    posts = cache.get(POSTS_KEY)
    if not posts:
        time.sleep(2)  # simulate a slow query.
        """Return the last five published posts."""
        posts = Post.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
        cache.set(POSTS_KEY, posts)

    def get_queryset(self):
        c = {'posts': posts}
        c.update(csrf(request)) 
        return  c

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())