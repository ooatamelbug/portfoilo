from django.urls import path
from .views import (
    User,
    About,
    Work,
    Service,
    Customer,
    Email,
    Language
)

urlpatterns = [
    path('user/', User.as_view(), name='user'),
    path('about/', About.as_view(), name='about'),
    path('work/', Work.as_view(), name='work'),
    path('service/', Service.as_view(), name='service'),
    path('customer/', Customer.as_view(), name='customer'),
    path('email/', Email.as_view(), name='email'),
    path('language/', Language.as_view(), name='language'),
]