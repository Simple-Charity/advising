from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):

    context = {
        
    }

    return render(request, "analyst/home.html", context)

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

    child_portfolio = ['A52','A6B','A6C','E86','G25','G61','G84','G98','H25','H61','H84','H98','I21','I70','I72','K30','N20','N30','N31','N32','O01','O02','O05','O11','O12','O19','O20','O21','O22','O23','O30','O31','O40','O41','O42','O43','O50','O51','O52','O53','O54','O55','O99','P30','P31','P32','P33','P40','P42','P43','P45','P46','P76','R28',]
    states = ["AR","TN","SC","NC","VA","WV","KY","IN","OH","MD","DE"]

    orgs = Organization.objects.filter(ntee_code__in=child_portfolio).filter(state__in=states)
    orgs = orgs | Organization.objects.filter(name__contains='child').filter(state__in=states) 
    orgs = orgs | Organization.objects.filter(name__contains='foster').filter(state__in=states) 
    orgs = orgs | Organization.objects.filter(name__contains='orphan').filter(state__in=states) 
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