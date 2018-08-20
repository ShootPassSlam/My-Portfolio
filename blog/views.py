from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

def index(request):
	return HttpResponse("This is where the blog goes")

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)