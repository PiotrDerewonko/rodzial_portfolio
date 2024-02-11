
from django.urls import path
from.views import home, about_me, contact

urlpatterns = [
    path('', home, name='home'),
    path('me', about_me, name='me'),
    path('contact', contact, name='contact'),
]