import os
os.environ.setdefault('DJANGO_SETTING_MODULE','firstproject.settings')
import django
django.setup()

#fake pop script
import random
from firstapp.models import AccessRecord,Webpage,Topic
from faker import Faker
fakegen=Faker()
Topics=['Search','Social','Marketplace','news','games']
def add_topic():
    t=Topic.objects.get_or_create(top=random.choice(Topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get topic for the entry
        top=add_topic()
        #create fake data

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #faek access AccessRecord
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ =='__main__':
    print("pop script")
    populate(20)
    print("pop complete")
