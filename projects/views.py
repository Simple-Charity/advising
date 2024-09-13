from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def projects_index(request):

    context = {
        'projects': Project.objects.all()
    }

    return render(request, "projects/project_index.html", context)

@login_required
def projects_entry(request, pid):

    active_project = Project.objects.get(id=pid)

    context = {
        'project': active_project,
        'orgs': active_project.organization_set.all().order_by('name') # type: ignore
    }

    return render(request, "projects/project_entry.html", context)