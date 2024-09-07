import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advising_database.settings")
django.setup()

from analyst.models import Organization

import datetime
import pytz

i=0
for org in Organization.objects.all():
    if org.updated_at:
        org.last_updated = datetime.datetime.strptime(org.updated_at, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.UTC)
        org.save()
    else:
        pass

    if i % 1000 == 0:
        print(i)
    i = i + 1

