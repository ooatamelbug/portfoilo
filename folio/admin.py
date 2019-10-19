from django.contrib import admin
from .models import (
    UserInfo,
    CustomerSaid,
    WorkExperience,
    LanguageSkill,
    ServiceProvider,
    AboutUser,
    SendEmail
)
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(CustomerSaid)
admin.site.register(WorkExperience)
admin.site.register(LanguageSkill)
admin.site.register(ServiceProvider)
admin.site.register(AboutUser)
admin.site.register(SendEmail)
