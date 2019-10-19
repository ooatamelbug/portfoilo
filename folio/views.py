# from django.shortcuts import render
# from rest_framework.response import Response
from .serializer import (
    UserInfoSerializer,
    WorkExperienceSerializer,
    LanguageSkillSerializer,
    AboutUserSerializer,
    CustomerSaidSerializer,
    ServiceProviderSerializer,
    SendEmailSerializer
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from .models import (
    UserInfo,
    CustomerSaid,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser,
    SendEmail
)

# Create your views here.


class User(ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class About(ListAPIView):
    queryset = AboutUser.objects.all()
    serializer_class = AboutUserSerializer


class Service(ListAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class Work(ListAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class Customer(ListAPIView):
    queryset = CustomerSaid.objects.all()
    serializer_class = CustomerSaidSerializer


class Language(ListAPIView):
    queryset = LanguageSkill.objects.all()
    serializer_class = LanguageSkillSerializer


class Email(CreateAPIView):
    queryset = SendEmail.objects.all()
    serializer_class = SendEmailSerializer
