from django.contrib import admin
from .models import ReferralUser, Referral

# Register your models here.
admin.site.register(Referral)
admin.site.register(ReferralUser)