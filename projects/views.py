from django.shortcuts import render

from django.http import HttpResponse

from .models import Project

def index(request):
	return HttpResponse("This is where the projects go")

def detail(request, post_id):
    return HttpResponse("You're looking at project %s." % project_id)