import os
os.environ.setdefault('DJANGO_SETTING_MODULE','firstproject.settings')
import django
django.setup()

#fake pop script
import random
from firstapp.models import AccessRecord,Webpage,Topic,Exe
from faker import Faker
fakegen=Faker()
Topics=['Search','Social','Marketplace','news','games']

def add_topic():

    t=Topic.objects.get_or_create(top=random.choice(Topics))[0]

    t.save()
    return t

def populate(N):
    for entry in range(N):

        #get topic for the entry
        top=add_topic()
        #create fake data



        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        fake_mail=fakegen.email()


        #create new webpage entry
        exe=Exe.objects.get_or_create(fname=fake_name,lname=fake_name,email=fake_mail)[0]

        exe.save()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #faek access AccessRecord
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ =='__main__':

    print("pop script")
    populate(20)
    print("pop complete")
