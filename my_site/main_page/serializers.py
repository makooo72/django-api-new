from rest_framework import serializers
from .models import Referral, ReferralUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('id', 'username', 'referral', )

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralUser
        fields = ('id', 'username', 'referral', )