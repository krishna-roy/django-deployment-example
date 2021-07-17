from django.contrib import admin
from polls.models import Voter,UserProfileInfo
# Register your models here.
admin.site.register(Voter)
admin.site.register(UserProfileInfo)
