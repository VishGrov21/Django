import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'testproject.settings')

import django
django.setup()

# Fake Population Script

import random
from first_proj.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    return Topic.objects.get_or_create(random.choice(topics))[0]


def populate(number_of_rows=20):

    # Populate Topics to the Topics model
    topic = add_topic()

    # Populating Webpage and AccessRecord Model
    for i in range(number_of_rows):
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_url = fakegen.url()

        #Populating Webpage
        webpage = Webpage.objects.get_or_create(topic = topic, name = fake_name, url = fake_url)[0]

        # Populating AccessRecord Model
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__=='__main__':
    print("Started Populating")
    populate(30)
    print("Data Population Successful !")
