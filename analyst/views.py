from django.shortcuts import render
from .models import *
import json

abbreviations = [
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States.
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY",
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Federal_district.
    "DC",
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Inhabited_territories.
    "AS", "GU", "MP", "PR", "VI",
]

abbreviation_to_name = {
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States.
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Federal_district.
    "DC": "District of Columbia",
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Inhabited_territories.
    "AS": "American Samoa",
    "GU": "Guam GU",
    "MP": "Northern Mariana Islands",
    "PR": "Puerto Rico PR",
    "VI": "U.S. Virgin Islands",
}

# Create your views here.
def home(request):

    context = {

    }

    return render(request, "analyst/home.html", context)

def org_detail(request,oid):

    context = {
        'org': Organization.objects.get(id=oid),
    }

    return render(request, "analyst/orgdetail.html", context)

def org_search(request):

    context = {
        'states': [{
            'name': abbreviation_to_name[a],
            'abbreviation': a,
        } for a in abbreviations ]
    }

    return render(request, "analyst/orgsearch.html", context)

def org_citylister(request):
    context = {
        'cities':sorted(set(org.city for org in Organization.objects.filter(state=request.POST.get('state-filter')))),
    }

    return render(request, "analyst/cityoutput.html", context)

def org_searchhelper(request):

    orgs = Organization.objects.all()
    if not request.POST.get('name-filter') == "":
        orgs = orgs.filter(name__contains=request.POST.get('name-filter'))
    if not request.POST.get('state-filter') == "":
        orgs = orgs.filter(state=request.POST.get('state-filter'))
    if not request.POST.get('city-filter') == "":
        orgs = orgs.filter(city=request.POST.get('city-filter'))

    context = {
        'message': request.POST.get('name-search-box'),
        'orgs': orgs,

    }

    return render(request, "analyst/orgsearchhelper.html", context)

def orgs_by_ntee(request,ntc):

    context = {
        'orgs': Organization.objects.filter(ntee_code=ntc).order_by('-revenue_amount')
    }

    return render(request, "analyst/orgs_by_ntee.html", context)

def orgs_by_state_city(request,given_state,given_city):

    context = {
        'orgs': Organization.objects.filter(state=given_state, city=given_city).order_by('-revenue_amount')
    }

    return render(request, "analyst/orgs_by_ntee.html", context)

def orgs_by_ein(request,ein_number):

    context = {
        'org': Organization.objects.get(ein=ein_number)
    }

    return render(request, "analyst/orgs_by_ein.html", context)

def orgs_cec(request):

    child_portfolio = ['A52','E86','G25','G61','G84','G98','H25','H61','H84','H98','I21','I70','I72','K30','N20','N30','N32','O01','O02','O05','O11','O12','O19','O20','O21','O22','O23','O30','O31','O40','O41','O42','O43','O50','O51','O52','O53','O54','O55','O99','P30','P31','P32','P33','P40','P42','P43','P45','P46','P76','R28',]
    states = ["AR","TN","SC","NC","VA","WV","KY","IN","OH","MD","DE"]

    orgs = Organization.objects.filter(ntee_code__in=child_portfolio).filter(state__in=states)
    orgs = orgs | Organization.objects.filter(name__contains='child').filter(state__in=states) 
    orgs = orgs | Organization.objects.filter(name__contains='foster').filter(state__in=states) 
    orgs = orgs | Organization.objects.filter(name__contains='orphan').filter(state__in=states) 
    orgs = orgs | Organization.objects.filter(name__contains='youth').filter(state__in=states) 
    orgs = orgs.filter(revenue_amount__gte=1000000)
    orgs = orgs.order_by('-revenue_amount')

    context = {
        'orgs': orgs,
    }

    return render(request, "analyst/orgs_by_ntee.html", context)

def orgs_by_revenue(request,rev_amount):

    context = {
        'orgs': Organization.objects.filter(revenue_amount__gte=rev_amount).order_by('-revenue_amount')
    }

    return render(request, "analyst/orgs_by_ntee.html", context)