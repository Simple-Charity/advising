from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from projects.models import *

@login_required
def home(request):

    context = {
    }

    return render(request, "analyst/home.html", context)

@login_required
def org_detail(request,oid):

    org = Organization.objects.get(id=oid)

    context = {
        'org': org,
        'search_string': "https://www.google.com/search?q=" + "+".join(org.name.split(" ")) + "+" + org.city + "+" + org.state,
        'all_projects': Project.objects.all().order_by('name'),
    }

    return render(request, "analyst/orgdetail.html", context)

@login_required
def org_search(request):

    context = {
        'states': [{
            'name': a.name,
            'abbreviation': a.postal_code,
        } for a in State.objects.all() ]
    }

    return render(request, "analyst/orgsearch.html", context)

@login_required
def org_citylister(request):
    state = request.POST.get('state-filter')
    context = {
        'cities':sorted([city.name for city in State.objects.get(postal_code = state).city_set.all()]), # type: ignore
    }

    return render(request, "analyst/cityoutput.html", context)

@login_required
def org_searchhelper(request):

    orgs = Organization.objects.all()
    if request.POST.get('name-filter'):
        orgs = orgs.filter(name__contains=request.POST.get('name-filter'))
    if request.POST.get('state-filter'):
        orgs = orgs.filter(state=request.POST.get('state-filter'))
    if request.POST.get('city-filter'):
        orgs = orgs.filter(city=request.POST.get('city-filter'))

    if request.POST.get('categorical-filter'):
        stype = request.POST.get('categorical-filter-options')
        modality = request.POST.get('categorical-filter-modalities')

        if stype == "nteecode":
            codes = [txt.strip() for txt in str(request.POST.get('categorical-filter')).split(",")]
            if modality == "isexactly":
                temp_orgs = Organization.objects.none()
                for code in codes:
                    temp_orgs = temp_orgs | orgs.filter(ntee_code__iexact=code)
                orgs = temp_orgs

                print(orgs)

            elif modality == "includes":
                temp_orgs = Organization.objects.none()
                for code in codes:
                    temp_orgs = temp_orgs | orgs.filter(ntee_code__contains=code)
                orgs = temp_orgs

            elif modality == "doesnotinclude":
                for code in codes:
                    orgs = orgs.filter(~Q(ntee_code__contains=code))

        elif stype == "activitycode":
            codes = [txt.strip() for txt in str(request.POST.get('categorical-filter')).split(",")]
            if modality == "isexactly":
                temp_orgs = Organization.objects.none()
                for code in codes:
                    temp_orgs = temp_orgs | orgs.filter(activity_codes__iexact=code)
                orgs = temp_orgs

            elif modality == "includes":
                temp_orgs = Organization.objects.none()
                for code in codes:
                    temp_orgs = temp_orgs | orgs.filter(activity_codes__contains=code)
                orgs = temp_orgs

            elif modality == "doesnotinclude":
                temp_orgs = Organization.objects.none()
                for code in codes:
                    orgs = orgs.filter(~Q(activity_codes__contains=code))
                orgs = temp_orgs
        


    if request.POST.get('quantitative-filter'):
        stype = request.POST.get('quantitative-filter-options')
        modality = request.POST.get('quantitative-filter-modalities')
        amount = request.POST.get('quantitative-filter')

        if stype == 'revenue':
            if modality == 'isgreaterthan':
                orgs = orgs.filter(revenue_amount__gt=amount)
            elif modality == 'islessthan':
                orgs = orgs.filter(revenue_amount__lt=amount)
            elif modality == 'isexactly':
                orgs = orgs.filter(revenue_amount=amount)
        elif stype == 'assets':
            if modality == 'isgreaterthan':
                orgs = orgs.filter(assets_amount__gt=amount)
            elif modality == 'islessthan':
                orgs = orgs.filter(assets_amount__lt=amount)
            elif modality == 'isexactly':
                orgs = orgs.filter(assets_amount=amount)
        elif stype == 'income':
            if modality == 'isgreaterthan':
                orgs = orgs.filter(income_amount__gt=amount)
            elif modality == 'islessthan':
                orgs = orgs.filter(income_amount__lt=amount)
            elif modality == 'isexactly':
                orgs = orgs.filter(income_amount=amount)

    context = {
        'message': request.POST.get('name-search-box'),
        'orgs': orgs.order_by('name'),

    }

    return render(request, "analyst/orgsearchhelper.html", context)

def system_status(request):

    context = {

    }

    return render(request, 'analyst/systemstatus.html')

@login_required
def project_helper_add_org_to_project(request):

    active_project = Project.objects.get(name = request.POST.get('projectselect'))
    active_org = Organization.objects.get(id = request.POST.get('org_id'))

    active_org.projects.add(active_project)
    active_org.save()


    context = {

    }

    return render(request, 'analyst/htmxhelpers/add_org_to_project.html', context)