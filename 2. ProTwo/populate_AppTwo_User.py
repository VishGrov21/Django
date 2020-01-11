import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import User

fakegen = Faker()

def add_user(number_of_rows=10):
    for i in range(number_of_rows):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__=='__main__':
    print("Started Populating")
    add_user(15)
    print("Data Population Successful !")
