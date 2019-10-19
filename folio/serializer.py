from .models import (
    UserInfo,
    CustomerSaid,
    SendEmail,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser
)
from rest_framework import (
    serializers
)


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class CustomerSaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSaid
        fields = '__all__'


class LanguageSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSkill
        fields = '__all__'


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'


class AboutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUser
        fields = '__all__'


class SendEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmail
        fields = '__all__'
