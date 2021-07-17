import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

from polls.models import User
from faker import Faker
import random

def populate():
    f=Faker()
    FName=f.first_name()
    LName=f.last_name()
    email=f.email().split('@')[1]
    email=FName+'.'+LName+str(random.randint(1970,2010))+'@'+email
    #print(FName,LName,email)

    t = User.objects.get_or_create(First_Name=FName,Last_Name=LName,Email_Id=email)[0]
    t.save()



if __name__ == '__main__':

    for i in range(50):
        populate()


