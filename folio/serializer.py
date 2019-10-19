from .models import (
    UserInfo,
    CustomerSaid,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser
)
from rest_framework import (
    serializers
)


class UserSerializer(serializers.ModelSerializer):
    class Mata:
        model = UserInfo
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Mata:
        model = WorkExperience
        fields = '__all__'


class CustomerSaidSerializer(serializers.ModelSerializer):
    class Mata:
        model = CustomerSaid
        fields = '__all__'


class LanguageSkillSerializer(serializers.ModelSerializer):
    class Mata:
        model = LanguageSkill
        fields = '__all__'


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Mata:
        model = ServiceProvider
        fields = '__all__'


class AboutUserSerializer(serializers.ModelSerializer):
    class Mata:
        model = AboutUser
        fields = '__all__'
