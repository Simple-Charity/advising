from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='analyst-home-page'),
    path('organizations/cec', views.orgs_cec, name='analyst-organization-cec'),
    path('organizations/ntee/<ntc>', views.orgs_by_ntee, name='analyst-organization-by-ntee-code'),
    path('organizations/ein/<ein_number>', views.orgs_by_ein, name='analyst-organization-by-ntee-code'),
    path('organizations/geography/<given_state>/<given_city>', views.orgs_by_state_city, name='analyst-organization-by-ntee-code'),
    path('organizations/revenue/<rev_amount>', views.orgs_by_revenue, name='analyst-organization-by-revenue'),
]
