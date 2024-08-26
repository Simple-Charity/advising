import requests, csv

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advising_database.settings")
django.setup()

import csv
from analyst.models import Organization

organizations = Organization.objects.all().order_by("ein")

api_root = "https://projects.propublica.org/nonprofits/api/v2/"

i=0
for org in organizations[200000:250000]:
    ein = org.ein

    url = api_root + "organizations/" + str(ein) + ".json"
    response = requests.get(url).json()["organization"]

    org.careofname = response['careofname']
    org.revenue_amount = response['revenue_amount']
    org.activity_codes = response['activity_codes']
    org.address = response['address']
    org.zipcode = response['zipcode']
    org.exemption_number = response['exemption_number']
    org.subsection_code = response['subsection_code']
    org.affiliation_code = response['affiliation_code']
    org.classification_codes = response['classification_codes']
    org.ruling_date = response['ruling_date']
    org.deductibility_code = response['deductibility_code']
    org.foundation_code = response['foundation_code']
    org.activity_codes = response['activity_codes']
    org.organization_code = response['organization_code']
    org.exempt_organization_status_code = response['exempt_organization_status_code']
    org.filing_requirement_code = response['filing_requirement_code']
    org.pf_filing_requirement_code = response['pf_filing_requirement_code']
    org.accounting_period = response['accounting_period']
    org.asset_amount = response['asset_amount']
    org.income_amount = response['income_amount']
    org.revenue_amount = response['revenue_amount']
    org.sort_name = response['sort_name']
    org.created_at = response['created_at']
    org.updated_at = response['updated_at']
    org.data_source = response['data_source']
    org.have_extracts = response['have_extracts']
    org.have_pdfs = response['have_pdfs']
    org.latest_object_id = response['latest_object_id']
    org.ntee_code = response['ntee_code']

    org.save()

    print(str(org.ein) + " - " + str(i))
    i = i + 1