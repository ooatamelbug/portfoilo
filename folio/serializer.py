from .models import (
    UserInfo,
    WorkHistory,
    EducationHistory,
    SendEmail,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser,
    TypeWork
)
from rest_framework import (
    serializers
)


class TypeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeWork
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    type = TypeWorkSerializer()

    class Meta:
        model = WorkExperience
        fields = ('id', 'title', 'desc', 'link', 'image', 'type','technology')


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
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
