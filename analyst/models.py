from django.db import models
import datetime

from projects.models import *

class State(models.Model):
    name = models.CharField(max_length=63)
    postal_code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=127)
    state = models.ForeignKey(
        State, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name + ", " + self.state.name
     


class Organization(models.Model):
    ein = models.CharField(max_length=9)
    name = models.CharField(max_length=1023)
    city = models.CharField(max_length=1023)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=63)
    indicator = models.CharField(max_length=15)

    hq_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    projects = models.ManyToManyField(Project)

    last_updated = models.DateTimeField(blank=True, null=True)

    careofname = models.CharField(max_length=255, blank=True, null=True)
    revenue_amount = models.IntegerField(blank=True, null=True)
    activity_codes = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    exemption_number = models.CharField(max_length=255, blank=True, null=True)
    subsection_code = models.CharField(max_length=255, blank=True, null=True)
    affiliation_code = models.CharField(max_length=255, blank=True, null=True)
    classification_codes = models.CharField(max_length=255, blank=True, null=True)
    ruling_date = models.CharField(max_length=255, blank=True, null=True)
    deductibility_code = models.CharField(max_length=255, blank=True, null=True)
    foundation_code = models.CharField(max_length=255, blank=True, null=True)
    organization_code = models.CharField(max_length=255, blank=True, null=True)
    exempt_organization_status_code = models.CharField(max_length=255, blank=True, null=True)
    tax_period = models.CharField(max_length=255, blank=True, null=True)
    asset_code = models.CharField(max_length=255, blank=True, null=True)
    income_code = models.CharField(max_length=255, blank=True, null=True)
    filing_requirement_code = models.CharField(max_length=255, blank=True, null=True)
    pf_filing_requirement_code = models.CharField(max_length=255, blank=True, null=True)
    accounting_period = models.CharField(max_length=255, blank=True, null=True)
    asset_amount = models.IntegerField(blank=True, null=True)
    income_amount = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.CharField(max_length=255, blank=True, null=True)
    data_source = models.CharField(max_length=255, blank=True, null=True)
    have_extracts = models.CharField(max_length=255, blank=True, null=True)
    have_pdfs = models.CharField(max_length=255, blank=True, null=True)
    latest_object_id = models.CharField(max_length=255, blank=True, null=True)
    ntee_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.hq_city:
            return self.name + " (" + self.hq_city.name + ", " + self.hq_city.state.postal_code + ")"
        else:
            return self.name