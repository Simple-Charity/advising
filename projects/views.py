from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def projects_index(request):

    context = {
        'projects': Project.objects.all()
    }

    return render(request, "analyst/project_index.html", context)

@login_required
def projects_entry(request, pid):

    context = {
        'project': Project.objects.get(id=pid)
    }

    return render(request, "analyst/project_entry.html", context)