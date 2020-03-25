from django.contrib import admin
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
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(WorkHistory)
admin.site.register(EducationHistory)
admin.site.register(WorkExperience)
admin.site.register(LanguageSkill)
admin.site.register(ServiceProvider)
admin.site.register(AboutUser)
admin.site.register(SendEmail)
admin.site.register(TypeWork)
