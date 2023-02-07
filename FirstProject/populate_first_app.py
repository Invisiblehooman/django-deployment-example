import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "FirstProject.settings")

import django

django.setup()

from faker import Faker
from first_app.models import User

fake = Faker()


def fake_users(n=5):
    for entry in range(n):
        fake_fname = fake.first_name()
        fake_lname = fake.last_name()
        fake_email = fake.email()
        # create user with fake data
        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    fake_users(20)
    print("Populating Complete!")


