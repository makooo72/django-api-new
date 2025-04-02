from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenerateReferralLink, RegisterUser, ReferralViewSet

router = DefaultRouter()
router.register("referrals", ReferralViewSet)

print(router.urls)

urlpatterns = [
    path('generate/', GenerateReferralLink.as_view(), name="generate_referral"),
    path('register/', RegisterUser.as_view(), name="register_user"),
    path('', include(router.urls))
]