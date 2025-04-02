from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import ReferralUser, Referral
from .serializers import ReferralSerializer, UserSerializer

class GenerateReferralLink(ListAPIView):
    serializer_class = ReferralSerializer

    def get_queryset(self):
        return Referral.objects.all()

    def post(self, request):
        user_id = request.data.get('username')
        user = Referral.objects.get(username=user_id)
        referral_code = request.data.get('referral')
        return Response({'referral_link': f'http://localhost:8000/register?ref={referral_code}'})


class RegisterUser(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return ReferralUser.objects.all()

    def post(self, request):
        referral_code = request.data.get('referral')
        if referral_code:
            referrer = ReferralUser.objects.get(referral=referral_code)
            new_user = ReferralUser.objects.create(username=request.data.get('username'))
            Referral.objects.create(user=referrer, referral_user=new_user)
            return Response({'message': 'Пользователь зарегистрирован'})
        else:
            referral_code_from_url = request.get_full_path().split("=")[-1]
            referrer = Referral.objects.get(id=referral_code_from_url)
            ReferralUser.objects.create(username=request.data.get('username'), referral=referrer)
            return Response({'message': 'Пользователь зарегистрирован'})



class ReferralViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ReferralSerializer
    queryset = Referral.objects.all()
    
