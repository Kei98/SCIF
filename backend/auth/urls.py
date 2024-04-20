from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login', login),
    path('test_token', test_token),


]

urlpatterns = format_suffix_patterns(urlpatterns)