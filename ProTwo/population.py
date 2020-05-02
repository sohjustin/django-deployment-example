import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegenerator = Faker()

def populate(N = 10):
    for element in range(N):

        fake_first_name = fakegenerator.first_name()
        fake_last_name = fakegenerator.last_name()
        fake_email = fakegenerator.email()

        User.objects.get_or_create(first_Name=fake_first_name, last_Name = fake_last_name, email = fake_email)[0]

if __name__ == '__main__':
    print("Populating...")
    populate(30)
    print("Populating Completed")
