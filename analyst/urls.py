from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='analyst-home-page'),
    path('orgsearchhelper', views.org_searchhelper, name='analyst-organization-searchhelper'),
    path('orgcitylister', views.org_citylister, name='analyst-organization-citylister'),
    path('organizations/detail/<oid>/', views.org_detail, name='analyst-organization-detail'),
    path('organizations/search/', views.org_search, name='analyst-organization-search'),
    path('systemstatus/', views.system_status, name='site-system-status'),
]
 