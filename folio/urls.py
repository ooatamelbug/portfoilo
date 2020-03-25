from django.urls import path
from .views import (
    User,
    About,
    Work,
    Service,
    Education,
    Workhistory,
    Email,
    Language,
    Type
)

urlpatterns = [
    path('user/', User.as_view(), name='user'),
    path('about/', About.as_view(), name='about'),
    path('work/', Work.as_view(), name='work'),
    path('service/', Service.as_view(), name='service'),
    path('education/', Education.as_view(), name='education'),
    path('workhistory/', Workhistory.as_view(), name='workhistory'),
    path('email/', Email.as_view(), name='email'),
    path('language/', Language.as_view(), name='language'),
    path('type/', Type.as_view(), name='type'),
]
