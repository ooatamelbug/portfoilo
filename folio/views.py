# from django.shortcuts import render
# from rest_framework.response import Response
from .serializer import (
    UserInfoSerializer,
    WorkExperienceSerializer,
    LanguageSkillSerializer,
    AboutUserSerializer,
    WorkHistorySerializer,
    EducationHistorySerializer,
    ServiceProviderSerializer,
    SendEmailSerializer,
    TypeWorkSerializer
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from .models import (
    UserInfo,
    WorkHistory,
    EducationHistory,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser,
    SendEmail,
    TypeWork
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


class Education(ListAPIView):
    queryset = EducationHistory.objects.all()
    serializer_class = EducationHistorySerializer


class Workhistory(ListAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer


class Language(ListAPIView):
    queryset = LanguageSkill.objects.all()
    serializer_class = LanguageSkillSerializer


class Email(CreateAPIView):
    queryset = SendEmail.objects.all()
    serializer_class = SendEmailSerializer


class Type(ListAPIView):
    queryset = TypeWork.objects.all()
    serializer_class = TypeWorkSerializer
