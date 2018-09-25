from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.core.cache import cache

from .models import Project

PROJECTS_KEY = "projects.all"

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        projects = cache.get(PROJECTS_KEY)
        if not projects:
            """Return the published projects."""
            projects = Project.objects.filter(project_date__lte=timezone.now())
            cache.set(PROJECTS_KEY, projects)
        return projects

def detail(request, post_id):
    return HttpResponse("You're looking at project %s." % project_id)