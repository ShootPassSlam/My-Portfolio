from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Project

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return the last five published projects."""
        return Project.objects.filter(
            project_date__lte=timezone.now()
        )

def detail(request, post_id):
    return HttpResponse("You're looking at project %s." % project_id)