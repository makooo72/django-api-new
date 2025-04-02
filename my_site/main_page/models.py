from django.db import models
from django.contrib.auth.models import User

class Referral(models.Model):
    username = models.CharField(max_length=100, blank=True, null=False)
    referral = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.referral

class ReferralUser(models.Model):
    username = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name="referral_code")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)