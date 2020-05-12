from faker import Faker
from second_app.models import WebUser
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()


fakegen = Faker()


def populate(N=5):
    for _ in range(N):
        fake_fName = fakegen.first_name()
        fake_lName = fakegen.last_name()
        fake_email = fakegen.email()
        user = WebUser.objects.get_or_create(
            first_name=fake_fName, last_name=fake_lName, email=fake_email)[0]
        user.save()


populate(40)
