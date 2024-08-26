import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advising_database.settings")
django.setup()

import csv
from analyst.models import Organization

for org in Organization.objects.all():
    org.delete()

with open('pub78 copy.txt') as f:
    csvr = csv.reader(f)
    all_charities = []
    i=0
    for row in csvr:
        charity_data = row[0].split("|")

        try:
            t_ein = charity_data[0]
        except: 
            t_ein = ""

        try:
            t_name = charity_data[1]
        except: 
            t_name = ""

        try:
            t_city = charity_data[2]
        except: 
            t_city = ""

        try:
            t_state = charity_data[3]
        except: 
            t_state = ""

        try:
            t_country = charity_data[4]
        except: 
            t_country = ""

        try:
            t_indicator = charity_data[5]
        except: 
            t_indicator = ""


        new_charity = Organization.objects.create(
            ein = t_ein,
            name = t_name,
            city = t_city,
            state = t_state,
            country = t_country,
            indicator = t_indicator,
        )

        new_charity.save()

        if i % 1000 == 0:
            print(i)
        i = i + 1
